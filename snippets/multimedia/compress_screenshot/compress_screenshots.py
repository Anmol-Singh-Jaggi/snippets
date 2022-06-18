import sys
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler): 
    def __init__(self): 
        super().__init__(patterns=['*.png'], ignore_directories=True, case_sensitive=False) 
  
    def on_created(self, event): 
        logging.debug("Watchdog received created event - % s." % event.src_path)
        self.compress_image(event.src_path)
    
    def compress_image(self, src_path):
        cmd = '/usr/local/bin/pngquant 128 --skip-if-larger --strip --ext=.png --force'
        cmd = cmd.split(" ")
        cmd.append(src_path)
        subprocess.run(cmd, stdout=subprocess.DEVNULL)
        cmd = '/usr/local/bin/zopflipng -y'
        cmd = cmd.split(" ")
        cmd.append(src_path)
        cmd.append(src_path[:-4] + '_compressed.png')
        #subprocess.run(cmd, stdout=subprocess.DEVNULL)

  

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = '/users/ajaggi/Screenshots'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while observer.isAlive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()