from __future__ import print_function

from os import listdir, rename
from os.path import isfile, join, getmtime, basename
import sys


def process_file_name(file_name, *args):
    sorted_file_name_list = args[0]
    file_order = sorted_file_name_list.index(file_name)
    new_file_name = str(file_order + 1).rjust(3, '0')
    return new_file_name


def main():
    input_directory_path = "."

    # Get the list of files in the input directory
    file_name_list = [file_name for file_name in listdir(
        input_directory_path) if isfile(join(input_directory_path, file_name))]
    file_name_list.remove(basename(sys.argv[0]))
    print(file_name_list, "\n\n\n")

    # Sort according to file-creation time
    sorted_file_name_list = sorted(file_name_list, key=getmtime)
    print(sorted_file_name_list, "\n\n\n")

    for index, file_name in enumerate(file_name_list):
        new_file_name = process_file_name(file_name, sorted_file_name_list)
        print(str(index + 1) + ") '" + file_name +
              "' --> '" + new_file_name + "'")
        if isfile(join(input_directory_path, new_file_name)):
            print("Error: Target name exists already!!")
            continue
        # Comment the following line to run a simulation
        #rename(file_name, new_file_name)

if __name__ == '__main__':
    main()
