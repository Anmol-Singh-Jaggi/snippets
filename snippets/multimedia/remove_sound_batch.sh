# Remove sound from videos
cd "folder_with_sound"
for file in *
do
    echo "${file}"
    ffmpeg -i "${file}" -c copy -an "../folder_without_sound/${file}";
done
