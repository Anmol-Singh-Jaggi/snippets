import re


def main():
    pattern = r"[a-zA-Z0-9][a-zA-Z0-9_.]{4,}@[a-zA-Z0-9]+\.(?:com|co\.in|org|edu)"
    pattern_compiled = re.compile(pattern)
    t = int(input())
    k = 0
    while t:
        t -= 1
        k += 1
        line = input()
        res = [i.group() for i in pattern_compiled.finditer(line)]

        case_str = "Case #" + str(k) + ": " + str(len(res))
        print(case_str)

        for i in res:
            print(i)


if __name__ == '__main__':
    main()
