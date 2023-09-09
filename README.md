# YTPlaylistsDownloader
![00004-1758643943](https://github.com/BaileyPillon/YTPlaylistsDownloader/assets/138253619/1ced8ad5-f6d2-4537-9f52-24eeaa872325)

- Downloads a list of YouTube playlists using yt-dlp. Downloads the following: .mp4 file, .mp3 file, .json file with metadata, thumbnail in .webp format.
- Embeds thumbnails to the .mp4 but not the .mp3. You can specify an output directory.
- If it doesn't exist, it's created. Subfolders within that directory are created based upon the uploader and the relevant aforementioned files are downloaded into those subfolders systematically. This can be easily altered if you don't care for that.
- Above image created with stable diffusion.

# INSPIRATION
- Getting tired of YouTube deleting all my favorite YouTube videos on the reg.
- Then just upload it to your mega account.

# REQUIREMENTS
- You can just need ffmpeg (and related files) plus yt-dlp which can be installed via pip install yt-dlp.
- ffmpeg can be downloaded here: https://ffmpeg.org/download.html directly or via source code and github repo (linked at the same location).
- yt-dlp can be downloaded here: https://github.com/yt-dlp/yt-dlp/releases
- yt-dlp is a fork of YouTubeDownloader.

# TO DO
- Ensure subtitles/captions are embedded and/or downloaded separately, if any exist.
- Scrape metadata for deleted or privated video (this can actually be done with few exceptions).
- Embed thumbnails to mp3 files, possibly convert mp4s to mp3s recursively using ffmpeg (it is a quick process) and modularize it in that sense.
- Upload latest yt-dlp and ffmpeg files here.
- Add parallelization (possibly) and general optimization.
- Requirements.txt (but there isn't much of one...)
- Taking suggestions.
