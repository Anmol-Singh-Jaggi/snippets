$next_file=python record-sequencer.py
ffmpeg -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" "$next_file"