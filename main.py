from __future__ import unicode_literals
import os
import yt_dlp

playlist_url = ['playlist1', 
                'playlist2',
                'playlist3',
                ...
                ]
                
def download_playlists(playlist):
    output_folder = os.makedirs(r'C:\path\to\directory', exist_ok=True)
    output_folder = r'C:\path\to\directory'
    
    ydl_opts = {
            #"format": "bestvideo[ext=mp4]+bestaudio[ext=mp4a]/best[ext=mp4]", 
            "format": "bestvideo+bestaudio/best",
            "ignoreerrors": True,
            "nooverwrites": True,
            "writethumbnail": True,
            "writeinfojson": True,
            "keepvideo": True,
            "matchtitle": "<insert keyword to match in partial or full>", # can comment out if you don't need this and simply want to DL every playlist video
            "verbose": True,
            "outtmpl": os.path.join(output_folder, "%(uploader)s/%(title)s.%(ext)s"),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'keepvideo': True,  
            'downloader_options': {
            'http_chunk_size': 1048576
        },
        'ffmpeg_location': r'C:\path\to\ffmpeg.exe' # can set path to ffmpeg or set it as a path variable
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist])

if __name__ == "__main__":
    for playlist in playlist_url:
        download_playlists(playlist)
        print("Done with one playlist!")
    print("Done with all playlists!")
