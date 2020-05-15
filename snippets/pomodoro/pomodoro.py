#!/usr/bin/env python3
'''
Run using the following command:
nohup python3 pomodoro.py &!
'''
import multiprocessing as mp
import subprocess
import time

dialog_message = "Break!!"
dialog_buttons = ["OK", "Snooze", "Finish"]
dialog_button_default = 2 # Snooze

cmd_dialog = "osascript -e 'tell app \"System Events\" to display dialog \"{}\" buttons {{\"{}\", \"{}\", \"{}\"}} default button {}'"
cmd_dialog = cmd_dialog.format(dialog_message, *dialog_buttons, dialog_button_default)

cmd_sound = "afplay /System/Library/Sounds/Tink.aiff"


INTERVAL_MINS=30
SNOOZE_MINS=5

def wait_for_mins(mins):
    time.sleep(mins*60)

def wait_for_secs(secs):
    time.sleep(secs)

def get_decreasing_seq():
    minl = 1
    curr = 5
    while True:
        yield curr
        curr = max(curr-1, minl)

def make_sound():
    for interval in get_decreasing_seq():
        # Start softly but go hard later.
        subprocess.run(cmd_sound, shell=True)
        wait_for_secs(interval)

def process_result(res):
    stdout = res.stdout.decode("utf-8")
    if res.returncode == 0:
        if "Finish" in stdout:
            exit()
        if "OK" in stdout:
            wait_time_mins = INTERVAL_MINS
        else:
            wait_time_mins = SNOOZE_MINS
    else:
        # No button was pressed and the dialog timed out.
        wait_time_mins = SNOOZE_MINS
    return wait_time_mins

def main():
    wait_time_mins = 30
    while True:
        wait_for_mins(wait_time_mins)
        sound_process = mp.Process(target=make_sound)
        sound_process.start()
        res = subprocess.run(cmd_dialog, shell=True, capture_output=True)
        sound_process.terminate()
        wait_time_mins = process_result(res)

main()