#!/usr/bin/env python3
'''
Run in background:
nohup python3 pomodoro.py &!
'''
import multiprocessing as mp

import setproctitle

from screen_state_observer import start_screen_state_observer
from main_loop import main_loop


def main():
    mp.set_start_method('spawn')
    setproctitle.setproctitle("pomodoro_root_process")

    screen_state_observer_process = mp.Process(name='pomodoro_screen_state_observer', target=start_screen_state_observer)
    screen_state_observer_process.start()

    main_loop_process = mp.Process(name='pomodoro_main_loop', target=main_loop)
    main_loop_process.start()

    # Bug: Root process not exiting, dont know why!
    exit(0)


if __name__ == '__main__':
    main()
