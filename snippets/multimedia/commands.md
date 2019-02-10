## Convert to avi keeping same quality (Just change the container; don't re-encode)
```
ffmpeg -i input.mp4 -codec copy output.avi
```

## Convert to avi (using the divX codec) keeping a decent quality
```
ffmpeg -i input.mp4 -c:v libxvid -qscale:v 6 output.avi
```

## Convert audio stream to mp3
```
ffmpeg -i input.mp4 -codec:v copy -codec:a libmp3lame output.mp4
```

## Remove audio
```
folder_with_sound="sound"
folder_without_sound="../nosound"

cd "${folder_with_sound}"
mkdir "${folder_without_sound}"


for file in *
do
    echo "${file}"
    ffmpeg -i "${file}" -c copy -an "${folder_without_sound}/${file}";
done
```

## Extract audio
```
# Assuming the audio format is m4a.
# If it is something else, change the output extension accordingly.
for file in *.mp4
do
    ffmpeg -i "${file}" -vn -acodec copy "audio/${file/.mp4/.m4a}";
done
```

## Concatenate multiple media files
```
# input.txt is of the following format:
#  file '/path/to/file1'
#  file '/path/to/file2'
#  file '/path/to/file3'
ffmpeg -f concat -i input.txt -c copy output
```

## Remove a segment of the video
```
# Remove the segment (1500 seconds - 1980 seconds)
ffmpeg -i input.mp4 -filter_complex \
"[0:v]trim=duration=1500[av]; \
    [0:a]atrim=duration=1500[aa];\
    [0:v]trim=start=1980,setpts=PTS-STARTPTS[bv]; \
    [0:a]atrim=start=1980,asetpts=PTS-STARTPTS[ba];\
    [av][bv]concat[outv]; [aa][ba]concat=v=0:a=1[outa]" \
    -map [outv] -map [outa] out.mp4
```

## Count number of frames in a video
```
ffmpeg -i in.mp4 -vcodec copy -f rawvideo -y /dev/null 2>&1 | tr ^M '\n' | awk '/^frame=/ {print $2}'|tail -n 1
```

## Record screen losslessly (screencast)
```
ffmpeg -f x11grab -s $(xrandr | grep '*' | awk '{print $1}') -framerate 15 -i :0.0 -c:v libx264 -preset veryslow -qp 0 out.mp4
```

## Extract frames from video
```
ffmpeg -i in.mp4 images/output_%04d.png
```

## Combine frames to video
```
ffmpeg -framerate 15 -pattern_type glob -i '*.png' -c:v libx264 -pix_fmt yuv420p -crf 35 -preset veryslow out.mp4
```

## Capture audio being played
- Install *pavucontrol*.
- Start recording with *ffmpeg*:  
`ffmpeg -f pulse -i default output.ogg`
- Start *pavucontrol*.
- Go to the *Recording* tab and you'll find *'ffmpeg'* or *'Lavf56.15.102'* (or similar) listed there.
- Change audio capture from *'Internal Audio Analog Stereo'* to *'Monitor of Internal Audio Analog Stereo'*.


## Convert ogg to mp3
```
folder_with_ogg_files="ogg_folder"
folder_with_mp3_files="../mp3_folder"

cd "${folder_with_ogg_files}"
mkdir "${folder_with_mp3_files}"

for file in *.ogg
do
    echo "${file}"
    ffmpeg -i "${file}" -c:a libmp3lame -q:a 2 "${folder_with_mp3_files}/${file/.ogg/.mp3}";
done
```

## Record screen with sound
```
ffmpeg -f gdigrab -i desktop -framerate 10 -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" -vcodec libx264 output.mp4
```

## Download Youtube videos
```
youtube-dl -f 137+140 <url of video>
137 and 140 are the format codes for 1080p video stream and the 128kbps audio stream respectively.
Sometimes webm will have even higher quality. Just execute 'youtube-dl -F <url>' to see all the format options.
```
