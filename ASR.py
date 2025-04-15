import os
import librosa
from pyannote.audio import Pipeline
from transformers import pipeline

# Fixed configuration (modify these according to your setup)
AUDIO_BASE_DIR = r"E:\Karya\Audio_outputs"  # From your file path example
AUDIO_EXTENSION = ".wav"  # Update if using different format

def generate_transcript(video_id):
    ## 1. Locate Audio File
    file_name = f"{video_id}{AUDIO_EXTENSION}"
    file_path = os.path.join(AUDIO_BASE_DIR, file_name)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found for video ID {video_id} at {file_path}")

    ## 2. Speaker Diarization Setup
    hf_token = os.environ.get('HF_TOKEN')
    diarization_pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=hf_token
    )

    ## 3. ASR Pipeline Configuration
    asr_pipeline = pipeline(
        "automatic-speech-recognition",
        model="ai4bharat/indicwav2vec-hindi",  # Using Hindi model from filename example
        device=-1
    )

    ## 4. Audio Processing
    full_audio, sr = librosa.load(file_path, sr=16000, mono=True)
    
    transcript = []
    for segment, _, speaker in diarization_pipeline(file_path).itertracks(yield_label=True):
        try:
            start_sample = int(segment.start * sr)
            end_sample = int(segment.end * sr)
            audio_segment = full_audio[start_sample:end_sample]

            result = asr_pipeline(
                audio_segment,
                return_timestamps='word', 
                chunk_length_s=30
            )

            transcript.append({
                "speaker": speaker,
                "start": round(segment.start, 2),
                "end": round(segment.end, 2),
                "text": result["text"].strip()
            })

        except Exception as e:
            print(f"Error in {segment.start}-{segment.end}: {str(e)}")
            continue

    return transcript

if __name__ == "__main__":
    file_path = "outputs/videoplayback.wav"
    transcript = generate_transcript(file_path)
    print(transcript)
