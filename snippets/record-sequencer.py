#!/usr/bin/env python3
'''
Outputs an available name for the recording output file.
'''

import os

def main():
    input_directory_path = "/home/anmol/Data/anmol/Downloads"

    x = 1
    while True:
        file_path = os.path.join(input_directory_path, str(x) + '.ogg')
        if not os.path.exists(file_path):
            break
        x = x+1
    print(file_path)

if __name__ == '__main__':
    main()
