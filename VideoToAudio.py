from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import os

def convert(video_path, output_format="mp3"):
    """
    Convert a video file to an audio file.
    
    Args:
        video_path (str): Path to the input video file.
        output_format (str): Desired audio format (e.g., "mp3", "wav").
        
    Returns:
        str: Path to the saved audio file.
    """
    # Check if the input file exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"The video file '{video_path}' does not exist.")
    
    output_directory = "outputs"
    
    os.makedirs(output_directory, exist_ok=True)
    
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_directory, f"{base_name}.{output_format}")
    video = VideoFileClip(video_path)
    
    if output_format == "mp3":
        codec = "libmp3lame"
    elif output_format == "wav":
        codec = "pcm_s16le"
    else:
        raise ValueError(f"Unsupported output format: {output_format}")
    
    video.audio.write_audiofile(audio_path, codec=codec)
    video.close()
    
    print(f"Conversion complete. Audio saved at: {audio_path}")
    return audio_path

if __name__ == "__main__":

    VIDEO_PATH = "inputs/videoplayback.mp4"  
    OUTPUT_FORMAT = "wav"
    
    try:
        convert(VIDEO_PATH, OUTPUT_FORMAT)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
