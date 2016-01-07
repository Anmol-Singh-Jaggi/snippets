import sys


def extract_number(line):
    number = ""
    for c in line:
        if c.isdigit():
            number += c
    return number


def get_next_name(input_file_lines, input_file_lines_iterator):
    name = ""
    while input_file_lines_iterator < len(input_file_lines):
        line = input_file_lines[input_file_lines_iterator]
        input_file_lines_iterator += 1
        if line[0:2] == "FN":
            name = line[3:]
            break
    return name, input_file_lines_iterator


def get_next_numbers(input_file_lines, input_file_lines_iterator):
    numbers = []
    while input_file_lines_iterator < len(input_file_lines):
        line = input_file_lines[input_file_lines_iterator]
        input_file_lines_iterator += 1
        if line[0:3] == "TEL":
            number = extract_number(line)
            numbers.append(number)
        else:
            break
    return numbers, input_file_lines_iterator


def main():
    input_file_path = sys.argv[1]
    input_file_handle = open(input_file_path)

    vcf_map = {}
    input_file_lines = input_file_handle.readlines()
    input_file_lines_iterator = 0
    while input_file_lines_iterator < len(input_file_lines):
        name, input_file_lines_iterator = get_next_name(
            input_file_lines, input_file_lines_iterator)
        numbers, input_file_lines_iterator = get_next_numbers(
            input_file_lines, input_file_lines_iterator)
        vcf_map.setdefault(name, []).extend(numbers)
        input_file_lines_iterator += 1

    vcf_map_sorted = sorted(vcf_map.items())
    for name, numbers in vcf_map_sorted:
        print name, numbers
    print "\n----- " + str(len(vcf_map)) + " records -----\n"

if __name__ == '__main__':
    main()
