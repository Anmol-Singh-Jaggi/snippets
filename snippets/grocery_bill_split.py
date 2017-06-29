#!/usr/bin/env python3


def main():
    entity_vs_amount = {}
    while True:
        # A line is of the format `num1 num2 num3 ... label-string`,
        # denoting that the amounts (num1 + num2 + num3) has to be
        # divided between the persons mentioned in the labels.
        # For example, `12 34 55 AS` => 101 has to be divided between 'A' and
        # 'S'.
        line = input()
        if not len(line):
            # Break on empty line.
            break
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
    print(entity_vs_amount)
    total_amount = sum(entity_vs_amount.values())
    print("Total amount = {}".format(total_amount))


if __name__ == '__main__':
    main()
