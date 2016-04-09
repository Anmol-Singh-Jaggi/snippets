# Convert to avi keeping same quality
    ffmpeg -i input.mp4 -codec copy output.avi

# Convert audio stream to mp3
    ffmpeg -i input.mp4 -codec:v copy -codec:a libmp3lame output.mp4

# Remove audio
    ffmpeg -i input.mp4 -c copy -an output.mp4

# Concatenate multiple media files
# input.txt is of the following format:
#   file '/path/to/file1'
#   file '/path/to/file2'
#   file '/path/to/file3'
    ffmpeg -f concat -i input.txt -c copy output

