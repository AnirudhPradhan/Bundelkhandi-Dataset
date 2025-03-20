import librosa
from pyannote.audio import Pipeline
import os
from transformers import pipeline

def generate_transcript(file_path):
    # Initialize the diarization pipeline
    hf_token = os.environ.get('HF_TOKEN')
    pipeline_diarization = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=hf_token
    )

    # Perform diarization
    diarization = pipeline_diarization(file_path)

    # Initialize the ASR model
    whisper_asr = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-large-v2",
    )

    transcript = []
    for segment, _, speaker in diarization.itertracks(yield_label=True):
        try:
            # Load audio segment
            audio, sr = librosa.load(
                file_path,
                sr=16000,
                offset=segment.start,
                duration=segment.duration,
                mono=True
            )

            # Perform ASR on the segment
            result = whisper_asr(
                audio,
                return_timestamps=True
            )

            # Extract text from the result
            text = result["text"]

            # Append segment information to the transcript
            transcript.append({
                "speaker": speaker,
                "start": float(segment.start),
                "end": float(segment.end),
                "text": text
            })

        except Exception as e:
            print(f"Failed segment {segment.start}-{segment.end}: {str(e)}")

    return transcript

if __name__ == "__main__":
    file_path = "outputs/videoplayback.wav"
    transcript = generate_transcript(file_path)
    print(transcript)
