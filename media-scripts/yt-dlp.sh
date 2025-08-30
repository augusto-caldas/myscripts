#!/usr/bin/env bash

# Check for --stream flag
STREAM=false
if [[ "$1" == "--stream" ]]; then
    STREAM=true
    shift
fi

SECTION=""

# Create section argument if not stream video
if [ "$STREAM" = false ]; then
    echo "Enter video start time (default: 00:00:00)"
    echo -n ">> "
    read -r START_TIME
    START_TIME=${START_TIME:-"00:00:00"}

    echo "Enter video end time (empty to download all)"
    echo -n ">> "
    read -r END_TIME

    SECTION="--download-sections *${START_TIME}-${END_TIME}"
fi

VIDEO_URL=""
while [ -z "$VIDEO_URL" ]; do
    echo "Enter YouTube video URL (cannot be empty)"
    echo -n ">> "
    read -r VIDEO_URL
done

# Download in one line
yt-dlp -P "$HOME/Videos" -o "%(title)s.%(ext)s" -f bestvideo*+bestaudio/best --merge-output-format mkv $SECTION "$VIDEO_URL"
