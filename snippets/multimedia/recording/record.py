#!/usr/bin/env python3
'''
Records the currently playing audio.
'''

from record_sequencer import get_available_path
from subprocess import run

available_path = get_available_path()
cmd = 'ffmpeg -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" "{}"'.format(available_path)
print("\nRecording at - '{}' ...\n".format(available_path))
run(cmd, shell=True)
