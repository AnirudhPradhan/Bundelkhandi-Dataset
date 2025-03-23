import yt_dlp
import os

def get_video(url, output_folder, format="mp4"):

    os.makedirs(output_folder, exist_ok=True)
    
    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  
        'merge_output_format': format,  
        'noplaylist': True,  
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  

# Example usage
video_url = "https://www.youtube.com/watch?v=25WmRh95luE"
output_folder = "inputs"
get_video(video_url, output_folder)
