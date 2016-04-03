from __future__ import print_function
import os


command = r'ls -d */ | cut --field=1 > dirs.temp'
os.system(command)
dirs = open('dirs.temp').readlines()

for i in dirs:
    i = "'" + i.strip()[:-1] + "'"
    command = 'cd ' + i + ' && git status'
    print(command)
    os.system(command)
    print("\n\n\n")
