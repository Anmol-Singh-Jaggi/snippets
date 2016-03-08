import re


text = "Hello, world. I'm a boy, you're a girl."

replaced = re.sub(
    '\S+', lambda m: re.match(r'^\W*(.*\w)\W*$', m.group()).group(1), text)

print(replaced)
