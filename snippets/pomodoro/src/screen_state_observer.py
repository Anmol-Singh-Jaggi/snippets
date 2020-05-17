#!/usr/bin/env python3
import multiprocessing as mp
import subprocess
import logging
logging.basicConfig(format='%(levelname)s:%(process)d:%(asctime)s:::%(message)s', datefmt='%d-%b-%y_%H:%M:%S', level=logging.DEBUG)
import Foundation
import AppKit
from PyObjCTools import AppHelper

import setproctitle

from main_loop import pkill, main_loop


class ScreenStateObserver(AppKit.NSObject):
    def screenOffHandler_(self, _):
        logging.debug('Killing main loop and its children')
        pkill('pomodoro_main_loop')
        pkill('pomodoro_make_sound')
        pkill('pomodoro_screen_off')

    def screenOnHandler_(self, _):
        logging.debug('Starting main loop again')
        cmd = "ps -ef | grep 'pomodoro_main_loop' | grep -v grep | awk '{print $2}'"
        res = subprocess.run(cmd, shell=True, capture_output=True)
        if len(res.stdout) > 0:
            logging.warn('Main loop already running!!', file=sys.stderr)
            return
        main_loop_process = mp.Process(name='pomodoro_main_loop', target=main_loop)
        main_loop_process.start()


def start_screen_state_observer():
    '''
    Kill the main loop whenever screen turns off, so that we dont keep getting dialogs and sounds
    even when laptop is unattended.
    Start the main loop again once screen is on again.
    '''
    logging.info('ScreenStateObserver process started.')
    setproctitle.setproctitle(mp.current_process().name)
    nc = Foundation.NSDistributedNotificationCenter.defaultCenter()
    screen_state_observer = ScreenStateObserver.new()
    nc.addObserver_selector_name_object_(screen_state_observer, 'screenOffHandler:', 'com.apple.screenIsLocked', None)
    nc.addObserver_selector_name_object_(screen_state_observer, 'screenOnHandler:', 'com.apple.screenIsUnlocked', None)
    AppHelper.runConsoleEventLoop()