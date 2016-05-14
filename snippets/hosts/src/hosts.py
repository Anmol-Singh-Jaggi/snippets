#!/usr/bin/env python3
from hosts_block_list import block_list


def main():
    block_list_processed = []
    for i in block_list:
        i += ".com"
        block_list_processed.append(i)
        block_list_processed.append("www." + i)

    block_list_string = "\n\n0.0.0.0"
    # print(block_string)

    for i in block_list_processed:
        block_list_string += " " + i

    block_list_string += "\n\n"

    print(block_list_string)


if __name__ == '__main__':
    main()
