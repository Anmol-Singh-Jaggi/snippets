import re


def main():
    pattern = r'[a-z]+'
    pattern = r'.*[.](?!bat$)[^.]*$'
    pattern = r'lol(?=abc)zz'

    pattern_compiled = re.compile(pattern)

    input = '123abc456def789ghi2456'
    input = 'abcdef.txt.bat'
    input = 'lolabczz'

    res = pattern_compiled.match(input)
    print(res)
    if res:
        print(res.group())
        print(res.span())

    res = pattern_compiled.search(input)
    print(res)
    if res:
        print(res.group())
        print(res.span())

    res = pattern_compiled.findall(input)
    print(res)

    res = pattern_compiled.finditer(input)
    print(res)
    for i in res:
        print(i)
        print(i.group())


if __name__ == '__main__':
    main()
