#!/usr/bin/env python3

'''
Takes a file containing environment variables and processes them
to make them ready for sourcing via cron.

Used for checking if a script is not running from cron due to absence
of any environment variables
'''


def main():
    # Generate this file by executing
    # `env > env-vars`
    env_file_path = 'env-vars'

    env_lines = open(env_file_path).readlines()

    for line in env_lines:
        line = line.strip()
        if not line:
            continue
        var, var_val = line.split('=', 1)
        print(line + '\nexport ' + var + '\n')


if __name__ == '__main__':
    main()
