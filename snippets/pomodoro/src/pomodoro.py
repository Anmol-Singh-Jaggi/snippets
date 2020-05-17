#!/usr/bin/env python3
'''
Run in background:
nohup python3 pomodoro.py &!
'''
import multiprocessing as mp
import logging
logging.basicConfig(format='%(levelname)s:%(process)d:%(asctime)s:::%(message)s', datefmt='%d-%b-%y_%H:%M:%S', level=logging.DEBUG)

import setproctitle

from screen_state_observer import start_screen_state_observer
from main_loop import main_loop


def main():
    # The default 'fork' is not compatible with ScreenStateObserver related OSX code.
    # No need once python is upgraded to 3.8+ on Mac since default is spawn since that version.
    mp.set_start_method('spawn')
    setproctitle.setproctitle("pomodoro_root_process")

    logging.info('Starting the root process...')

    screen_state_observer_process = mp.Process(name='pomodoro_screen_state_observer', target=start_screen_state_observer)
    screen_state_observer_process.start()

    main_loop_process = mp.Process(name='pomodoro_main_loop', target=main_loop)
    main_loop_process.start()

    # Bug: Root process not exiting, dont know why!
    exit(0)


if __name__ == '__main__':
    main()
