input_file_path = "in.txt"
output_file_path = "out.txt"


def main():
    input_file_handle = open(input_file_path)
    output_file_handle = open(output_file_path, "w")

    for line in input_file_handle.readlines():
        print >>output_file_handle, "    " + line,

if __name__ == "__main__":
    main()
