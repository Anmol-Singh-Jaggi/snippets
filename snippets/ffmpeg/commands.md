## Convert to avi keeping same quality
    ffmpeg -i input.mp4 -codec copy output.avi

## Convert audio stream to mp3
    ffmpeg -i input.mp4 -codec:v copy -codec:a libmp3lame output.mp4

## Remove audio
    ffmpeg -i input.mp4 -c copy -an output.mp4


## Extract audio
    # Assuming the audio format is m4a.
    # If it is something else, change the output extension accordingly.
    ffmpeg -i input.mp4 -vn -acodec copy output.m4a
    
    # The batch version of the above command.
    for file in *.mp4
    do
       ffmpeg -i "${file}" -vn -acodec copy "audio/${file%.*}.m4a";
    done


## Concatenate multiple media files
    ffmpeg -f concat -i input.txt -c copy output
    # input.txt is of the following format:
    #  file '/path/to/file1'
    #  file '/path/to/file2'
    #  file '/path/to/file3'

## Remove a segment of the video
    # Remove the segment (1500 seconds - 1980 seconds)
    ffmpeg -i input.mp4 -filter_complex \
    "[0:v]trim=duration=1500[av]; \
     [0:a]atrim=duration=1500[aa];\
     [0:v]trim=start=1980,setpts=PTS-STARTPTS[bv]; \
     [0:a]atrim=start=1980,asetpts=PTS-STARTPTS[ba];\
     [av][bv]concat[outv]; [aa][ba]concat=v=0:a=1[outa]" \
     -map [outv] -map [outa] out.mp4
