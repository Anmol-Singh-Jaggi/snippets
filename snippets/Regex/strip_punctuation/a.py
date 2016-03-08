import re


text = "Hello, world. I'm a boy, you're a girl."

replaced = re.sub('\S+', lambda m: re.sub('^\W+|\W+$', '', m.group()), text)

print(replaced)
