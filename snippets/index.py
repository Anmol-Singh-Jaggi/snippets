'''
A program used for indexing(numbering) exam notes.

Sample input -:

blah
 blah
  blah
  blah
 blah
  blah
   blah
    blah

Sample Output -:

1) blah
 1.1) blah
  1.1.1) blah
  1.1.2) blah
 1.2) blah
  1.2.1) blah
   1.2.1.1) blah
    1.2.1.1.1) blah
'''


def get_depth(line):
    i = 0
    while line[i] == ' ':
        i += 1
    return i


def depth_right(index):
    return index + ".0"


def depth_left(index):
    pos = index.rfind(".")
    return index[:pos]


def increment(index):
    pos = index.rfind(".")
    num = index[pos + 1:]
    num = int(num)
    num += 1
    ret = str(num)
    if pos >= 0:
        ret = index[:pos] + "." + ret
    return ret


def process_file(file_handle, starting_index="0"):
    index = starting_index
    prev_line_depth = 0
    curr_line_depth = 0
    for line in file_handle:
        curr_line_depth = get_depth(line)
        if curr_line_depth > prev_line_depth:
            index = depth_right(index)
        elif curr_line_depth < prev_line_depth:
            diff = prev_line_depth - curr_line_depth
            for i in xrange(diff):
                index = depth_left(index)
        index = increment(index)
        print " " * curr_line_depth + index + ") " + line.strip()
        prev_line_depth = curr_line_depth


def main():
    # First generate notes of every chapter in a separate file.
    # Then combine all of them into one 'in.txt' by running the commands
    # 'cat [1-10].txt' (assumming 10 chapters).
    filename = "in.txt"
    file_handle = open(filename)
    process_file(file_handle)

if __name__ == "__main__":
    main()
