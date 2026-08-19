# YouTube Downloader for Termux

A simple command-line YouTube downloader written in Python for **Termux on Android**.

Supports:

* 🎬 YouTube videos
* 📱 YouTube Shorts
* 📋 YouTube playlists
* 🎵 MP3 audio
* 🎥 MP4 video
* 🎞️ AVI video
* 🎧 OGG audio
* 🖼️ GIF animation

Downloaded files are saved automatically to:

```text
/sdcard/Download
```

---

## Requirements

* Android
* Termux
* Python 3
* FFmpeg
* yt-dlp
* Storage permission for Termux

---

## Installation

### 1. Update Termux

```bash
pkg update -y
pkg upgrade -y
```

### 2. Install Python and FFmpeg

```bash
pkg install python ffmpeg -y
```

### 3. Give Termux access to Android storage

```bash
termux-setup-storage
```

When Android asks for permission, select **Allow**.

### 4. Install Python dependencies

If you have the included `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or install yt-dlp directly:

```bash
pip install -U "yt-dlp[default]"
```

---

## Usage

Start the downloader:

```bash
python youtube_downloader.py
```

The program will ask for a YouTube URL:

```text
Entrez le lien YouTube :

> https://www.youtube.com/watch?v=XXXXXXXX
```

Then select one of the five formats:

```text
[1] MP3  - Audio
[2] MP4  - Vidéo
[3] AVI  - Vidéo
[4] OGG  - Audio
[5] GIF  - Animation

> 2
```

The program will ask for confirmation before starting the download.

---

## Output directory

All downloaded files are stored in:

```text
/sdcard/Download/
```

You can access them from Android's file manager under:

```text
Internal Storage
└── Download
```

---

## Playlists

You can enter a playlist URL directly:

```text
https://www.youtube.com/playlist?list=XXXXXXXX
```

yt-dlp will process the playlist automatically.

Playlist files are numbered when appropriate:

```text
1 - Video One [abc123].mp4
2 - Video Two [def456].mp4
3 - Video Three [ghi789].mp4
```

---

## Supported formats

| Option | Format | Description            |
| ------ | ------ | ---------------------- |
| 1      | `.mp3` | Audio only             |
| 2      | `.mp4` | Video                  |
| 3      | `.avi` | Video converted to AVI |
| 4      | `.ogg` | Audio only             |
| 5      | `.gif` | Video converted to GIF |

### MP3

Downloads the best available audio and converts it to MP3.

### MP4

Downloads the best available video and audio and combines them into an MP4 file using FFmpeg.

### AVI

Downloads the video and converts it to AVI using FFmpeg.

### OGG

Extracts the audio and converts it to OGG/Vorbis.

### GIF

Converts the video into an animated GIF. The downloader limits the source video to approximately 480p to help prevent excessively large GIF files.

---

## Updating yt-dlp

YouTube changes frequently, so keeping yt-dlp updated is recommended:

```bash
pip install -U "yt-dlp[default]"
```

Check the installed version:

```bash
yt-dlp --version
```

---

## Troubleshooting

### `yt-dlp: command not found`

Install yt-dlp:

```bash
pip install -U "yt-dlp[default]"
```

### `ffmpeg: command not found`

Install FFmpeg:

```bash
pkg install ffmpeg -y
```

### Permission denied for `/sdcard/Download`

Run:

```bash
termux-setup-storage
```

Then allow Termux to access your files.

You can verify the directory with:

```bash
ls /sdcard/Download
```

### YouTube download fails

First update yt-dlp:

```bash
pip install -U "yt-dlp[default]"
```

Then try again.

---

## Project structure

```text
youtube-downloader/
│
├── youtube_downloader.py
├── requirements.txt
└── README.md
```

---

## Quick installation

For a fresh Termux installation:

```bash
pkg update -y
pkg upgrade -y
pkg install python ffmpeg -y
termux-setup-storage
pip install -U "yt-dlp[default]"
```

Then:

```bash
python youtube_downloader.py
```

---

## Legal / Responsible Use

This tool is intended for downloading content that you are authorized to download.

Respect:

* YouTube's Terms of Service
* Copyright laws
* The rights of content creators
* Any applicable restrictions on the videos you download

Do not use the program to bypass DRM, access private content, or download copyrighted material without appropriate permission.
