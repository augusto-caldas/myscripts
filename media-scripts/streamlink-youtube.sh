# Keep asking until a URL is entered
VIDEO_URL=""
while [ -z "$VIDEO_URL" ]; do
    echo "Enter YouTube video URL (cannot be empty)"
    echo -n ">> "
    read -r VIDEO_URL
done

streamlink "$VIDEO_URL" best --player mpv
