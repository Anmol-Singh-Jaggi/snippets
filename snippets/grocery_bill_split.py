#!/usr/bin/env python3
import sys
import traceback


def process(lines):
    entity_vs_amount = {}
    for line in lines:
        # A line is of the format `num1 num2 num3 ... label-string`,
        # denoting that the amounts (num1 + num2 + num3) has to be
        # divided between the persons mentioned in the labels.
        # For example, `12 34 55 AS` => 101 has to be divided between 'A' and
        # 'S'.
        line = line.split()
        assert(len(line) > 1)
        amounts = line[:-1]
        entities = line[-1]
        amount = sum(float(num) for num in amounts)
        amount_per_entity = float(amount) / len(entities)
        for entity in entities:
            entity_amount = entity_vs_amount.get(entity, 0)
            entity_amount += amount_per_entity
            entity_vs_amount[entity] = entity_amount
    return entity_vs_amount


def get_input_from_stdin():
    lines = []
    while True:
        line = input()
        if not len(line):
            # Break on empty line.
            break
        lines.append(line)
    return lines


def main():
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        with open(input_file_path) as input_file:
            lines = input_file.readlines()
    else:
        lines = get_input_from_stdin()
    try:
        entity_vs_amount = process(lines)
        print(entity_vs_amount)
        total_amount = sum(entity_vs_amount.values())
        print("Total amount = {}".format(total_amount))
    except Exception:
        exception_traceback = traceback.format_exc()
        print("Error while processing input:\n\n---- start ----\n{}\n---- end ----\n\nwith the following exception trace:\n{}".format(
            lines, exception_traceback))


if __name__ == '__main__':
    main()
