#!/bin/bash
# A script to record your screen to a video/gif using byzanz-record.

# Sound notification to let one know when recording is about to start (and ends)
beep() {
    paplay /usr/share/sounds/ubuntu/stereo/system-ready.ogg &
}

# Delay before starting
DELAY=1
# How long to record
DURATION=120

echo "Delaying $DELAY seconds."
for (( i=$DELAY; i>0; --i )) ; do
    echo $i
    sleep 1
done

beep
# Ending beep scheduled beforehand as the main program can take
# quite some time to do post-processing (encoding, writing to file)
# after finishing the recording.
{ sleep $DURATION; beep; } &
byzanz-record --cursor --verbose --delay=0 --duration=$DURATION /home/anmol/Desktop/out.gif
