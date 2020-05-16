#!/usr/bin/env python3
'''
Run in background:
nohup python3 pomodoro.py &!
'''
import multiprocessing as mp
import subprocess

import setproctitle
import Quartz
import Foundation
from AppKit import *
from PyObjCTools import AppHelper

from main_loop import main_loop, wait_for_secs, pkill


SCREEN_MONITOR_INTERVAL_SECS = 5


def is_screen_off():
    session_dict = Quartz.CGSessionCopyCurrentDictionary()
    return session_dict.get("CGSSessionScreenIsLocked", 0) == 1


def exit_if_screen_on():
    setproctitle.setproctitle(mp.current_process().name)
    while True:
        if not is_screen_off():
            print('Exiting since screen on')
            exit(0)
        wait_for_secs(SCREEN_MONITOR_INTERVAL_SECS)


def exit_if_screen_off():
    setproctitle.setproctitle(mp.current_process().name)
    while True:
        if is_screen_off():
            print('Exiting since screen off')
            exit(0)
        wait_for_secs(SCREEN_MONITOR_INTERVAL_SECS)


def loop_screen_off():
    setproctitle.setproctitle(mp.current_process().name)
    while True:
        if is_screen_off():
            print('Killing main loop and its children')
            pkill('pomodoro_main_loop')
            # For some reason its children are not being killed
            # automatically on parent's death, despite them being daemon.
            # Hence, have to kill them manually.
            pkill('pomodoro_make_sound')
            pkill('pomodoro_screen_off')
            exit_if_screen_on_process = mp.Process(name='pomodoro_exit_if_screen_on', target=exit_if_screen_on)
            exit_if_screen_on_process.start()
            exit_if_screen_on_process.join()
        else:
            print('Waiting for screen to turn off...')
            exit_if_screen_off_process = mp.Process(name='pomodoro_exit_if_screen_off', target=exit_if_screen_off)
            exit_if_screen_off_process.start()
            exit_if_screen_off_process.join()


def loop_screen_on():
    setproctitle.setproctitle(mp.current_process().name)
    while True:
        if not is_screen_off():
            print('Starting main loop')
            main_loop_process = mp.Process(name='pomodoro_main_loop', target=main_loop)
            main_loop_process.start()
            exit_if_screen_off_process = mp.Process(name='pomodoro_exit_if_screen_off', target=exit_if_screen_off)
            exit_if_screen_off_process.start()
            exit_if_screen_off_process.join()
        else:
            print('Waiting for screen to turn on...')
            exit_if_screen_on_process = mp.Process(name='pomodoro_exit_if_screen_on', target=exit_if_screen_on)
            exit_if_screen_on_process.start()
            exit_if_screen_on_process.join()
            main_loop_process.join()