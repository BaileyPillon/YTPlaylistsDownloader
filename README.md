# YTPlaylistsDownloader
![00004-1758643943](https://github.com/BaileyPillon/YTPlaylistsDownloader/assets/138253619/1ced8ad5-f6d2-4537-9f52-24eeaa872325)

- Downloads a list of YouTube playlists using yt-dlp. Downloads the following: .mp4 file, .mp3 file, .json file with metadata, and thumbnail in .webp format.
- Tested on: Python 3.10.9 in a virtualenv, yt-dlp version: 2023.07.06, and ffmpeg version: 2023-09-07-git-9c9f48e7f2
- The "playlist" link can be an actual playlist link but it can also point to specific channels and their videos page as a "playlist" link.
- Embeds thumbnails to the .mp4 but not the .mp3. You can specify an output directory.
- If it doesn't exist, it's created. Subfolders within that directory are created based upon the uploader and the relevant aforementioned files are downloaded into those subfolders systematically. This can be easily altered if you don't care for that.
- It will download the highest quality video for video and audio given by: "format": "bestvideo+bestaudio/best" then merge it into an .mp4. If you don't want the highest quality available then comment that out and subtitute with "format": "bestvideo[height<=?1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" - this will download the best quality videos up to 1080p (if available) and may be modified to 720, 1440, or 2160. In practice, I think excluding "[ext=m4a]" next to bestaudio might be better, but I'm not currently sure.
- Above image created with stable diffusion.

# INSPIRATION
- Getting tired of YouTube deleting all my favorite YouTube videos (more specifically songs) on the reg.
- Then just upload it to your mega account: https://mega.nz

# REQUIREMENTS
- You can just need ffmpeg (and related files) plus yt-dlp which can be installed via pip install yt-dlp, see here: https://pypi.org/project/yt-dlp/
- yt-dlp can be downloaded directly here: https://github.com/yt-dlp/yt-dlp/releases
- yt-dlp is a fork of YouTubeDownloader (yt-dl)
- ffmpeg can be downloaded here: https://ffmpeg.org/download.html directly or via source code and github repo (linked at the same location).
  
# TO DO
- Ensure subtitles/captions are embedded and/or downloaded separately, if any exist.
- Scrape metadata for deleted or privated video (this can actually be done with few exceptions).
- Embed thumbnails to mp3 files, possibly convert mp4s to mp3s recursively using ffmpeg (it is a quick process) and modularize it in that sense.
- Upload latest yt-dlp and ffmpeg files here.
- Add parallelization (possibly) and general optimization.
- Add more params and make it customizable via CLI.
- Requirements.txt (but there isn't much of one...)
- Authentication for private playlists and obfuscation of credentials.
- Automated uploading of .mp3 files to AWS account S3 bucket and transcription of .mp3 files.
- Taking suggestions.
