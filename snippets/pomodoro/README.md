# Intro

- A python script running in an infinite loop, which will display a dialog on the screen periodically to force you to take breaks.
- You are supposed to work without distractions for 30 minutes and then take a break for 5 minutes.
- The script will sleep for 30 minutes if you press `OK` and 5 minutes if you press `Snooze` (helpful if you want to extend the current working session for some reason).
- The dialog box is intentionally obtrusive and cannot be minimized or hidden until you press a button.
- It also keeps generating a sound until a button is pressed.
- To not the see the dialog ever again, press `Finish` to kill the script.

![screenshot](screenshot-pomodoro.png)

# Setup

Execute it manually and run in background:
```
nohup python3 pomodoro.py &!
```

To make it run automatically at startup:
1. Configure the `.plist` file as per your needs:
    - Overwrite `'ajaggi'` with your username.
    - Modify the script location (`/users/ajaggi/Documents/personal/scripts/pomodoro.py`) to the right value.
2. Copy the plist file to `~/Library/LaunchAgents`.