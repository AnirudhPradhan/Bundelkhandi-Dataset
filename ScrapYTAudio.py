import yt_dlp
import os
import csv
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('api_key1')

def get_audio(url, output_folder, csv_file, language):
    """
    Downloads audio from a YouTube video and stores metadata in a CSV file.

    Args:
        url (str): URL of the YouTube video.
        output_folder (str): Folder to save the WAV file.
        csv_file (str): CSV file to store metadata.
    """
    os.makedirs(output_folder, exist_ok=True)

    # yt-dlp options for downloading audio
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(id)s.%(ext)s'),  # Output template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'wav',  # Output format set to WAV
        }],
        'noplaylist': True,  # Skip playlists
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Downloaded and saved as WAV: {info['title']}")

            # Extract video ID from URL
            video_id = info['id']

            # Retrieve metadata using YouTube Data API
            metadata = get_video_information(video_id,language)

            # Write metadata to CSV file
            write_metadata_to_csv(metadata, csv_file)
            
    except Exception as e:
        print(f"Error: {e}")

def get_video_information(video_id,language):
    """
    Retrieves metadata of a YouTube video using the YouTube Data API.

    Args:
        video_id (str): ID of the YouTube video.

    Returns:
        dict: Metadata including video ID, title, channel ID, and published date.
    """
    youtube = build("youtube", "v3", developerKey=API_KEY)

    response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()

    if "items" in response and len(response["items"]) > 0:
        snippet = response["items"][0]["snippet"]
        
        # Fetch AI training status
        trainability_response = youtube.videoTrainability().get(
            id=video_id
        ).execute()

        # Extract trainability status
        ai_training_status_list = trainability_response.get('permitted', ['Unknown'])
        # if ai_training_status_list[0] == 'PERMITTED':
        #     ai_training_status = 'Permitted'
        # elif ai_training_status_list[0] == 'NOT_PERMITTED':
        #     ai_training_status = 'Not Permitted'
        # else:   
        #     ai_training_status = 'Unknown'

        return {
            "Video ID": video_id,
            "Title": snippet["title"],
            "Channel ID": snippet["channelId"],
            "Published Date": snippet["publishedAt"],
            "Language": language,
            "AI Training Status": ai_training_status_list[0],
        }
    else:
        return None

def write_metadata_to_csv(metadata, csv_file):
    """
    Writes video metadata into a CSV file.

    Args:
        metadata (dict): Video metadata.
        csv_file (str): Path to the CSV file.
    """
    if not metadata:
        print("No metadata available.")
        return

    # Check if the CSV file exists
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Video ID", "Title", "Channel ID", "Published Date","Language","AI Training Status"])
        
        # Write header only if the file doesn't exist
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(metadata)
        print(f"Metadata saved to {csv_file}")

if __name__ == "_main_":
    url = "https://www.youtube.com/watch?v=bYGY1s6VMWs"
    output_folder = "audio_outputs"
    csv_file = "video_metadata.csv"

    get_audio(url, output_folder, csv_file)