import librosa
from pyannote.audio import Pipeline
import os
from transformers import pipeline

def generate_transcript(file_path):
    # Initialize diarization pipeline
    hf_token = os.environ.get('HF_TOKEN')
    pipeline_diarization = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=hf_token
    )

    # Initialize AI4Bharat ASR pipeline for Odia
    asr_pipeline = pipeline(
        "automatic-speech-recognition",
        # model="ai4bharat/indicwav2vec-hindi" #use this for generating hindi transcripts
        model="ai4bharat/indicwav2vec-odia" # use this for generating odia transcripts
    )

    # Perform diarization
    diarization = pipeline_diarization(file_path)

    transcript = []
    for segment, _, speaker in diarization.itertracks(yield_label=True):
        try:
            # Load audio segment
            audio, sr = librosa.load(
                file_path,
                sr=16000,  # Ensure 16kHz sampling rate
                offset=segment.start,
                duration=segment.duration,
                mono=True
            )

            # Perform ASR on segment
            result = asr_pipeline(audio,
                                  return_timestamps='word')

            # Append structured results
            transcript.append({
                "speaker": speaker,
                "start": round(float(segment.start), 2),
                "end": round(float(segment.end), 2),
                "text": result["text"].strip()
            })

        except Exception as e:
            print(f"Error processing {segment.start}-{segment.end}: {str(e)}")

    return transcript

if __name__ == "__main__":
    file_path = "outputs/videoplayback.wav"
    transcript = generate_transcript(file_path)
    print(transcript)
