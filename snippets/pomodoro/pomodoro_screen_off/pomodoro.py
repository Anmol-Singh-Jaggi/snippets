#!/usr/bin/env python3
'''
Run in background:
nohup python3 pomodoro.py &!
'''
import multiprocessing as mp
from screen_loop import loop_screen_off, loop_screen_on


def main():
    loop_screen_off_process = mp.Process(name='pomodoro_loop_screen_off', target=loop_screen_off)
    loop_screen_off_process.start()

    loop_screen_on_process = mp.Process(name='pomodoro_loop_screen_on', target=loop_screen_on)
    loop_screen_on_process.start()


if __name__ == '__main__':
    main()
