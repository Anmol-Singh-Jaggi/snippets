#!/usr/bin/env python3
'''
Generates the original non-indexed version of notes.
'''

import re


def main():
    lines = open('out.txt').readlines()
    for line in lines:
        print(re.sub(r'\d.*?\) ', '', line), end='')


if __name__ == '__main__':
    main()
