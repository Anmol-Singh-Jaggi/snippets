#!/usr/bin/env python3
'''
Outputs an available name for the recording output file.
'''

import os, errno


def mkdir_p(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def get_available_path():
    recordings_directory_path = "D:/Downloads/recordings/"

    x = 1
    while True:
        file_path = recordings_directory_path + str(x) + '.ogg'
        if not os.path.exists(file_path):
            break
        x = x+1

    mkdir_p(recordings_directory_path)
    return file_path


def main():
    print(get_available_path())


if __name__ == '__main__':
    main()
