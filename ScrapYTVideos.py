import yt_dlp
import os

def get_video(url, output_folder, format="mp4"):
    """
    Downloads a video using yt-dlp and merges video/audio streams with FFmpeg.

    Args:
        url (str): URL of the video to download.
        output_folder (str): Folder where the downloaded video will be saved.
        format (str): Output format (default is 'mp4').
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Output file template
        'merge_output_format': format,  # Merge streams into specified format
        'postprocessors': [{  # Ensure FFmpeg is used for merging
            'key': 'FFmpegVideoConvertor',
            'preferedformat': format,
        }],
        'noplaylist': True,  # Avoid downloading playlists
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video
        print("Video download completed successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage


if __name__ == "_main_":
    video_url = "https://www.youtube.com/watch?v=TPhneXSoZ6E"  # Replace with your video URL
    output_folder = "downloads"  # Replace with your desired output folder path
    get_video(video_url, output_folder)