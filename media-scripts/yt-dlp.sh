#!/usr/bin/env bash

echo "Enter video start time (default: 00:00:00)"
echo -n ">> "
read -r START_TIME
START_TIME=${START_TIME:-"00:00:00"}

echo "Enter video end time (empty to download all)"
echo -n ">> "
read -r END_TIME

# Keep asking until a URL is entered
VIDEO_URL=""
while [ -z "$VIDEO_URL" ]; do
    echo "Enter YouTube video URL (cannot be empty)"
    echo -n ">> "
    read -r VIDEO_URL
done

# Build section argument
SECTION="*${START_TIME}-${END_TIME}"

# Download
yt-dlp -P "$HOME/Videos" -o "%(title)s.%(ext)s" -f bestvideo*+bestaudio/best --merge-output-format mkv --download-sections "*${START_TIME}-${END_TIME}" "$VIDEO_URL"
