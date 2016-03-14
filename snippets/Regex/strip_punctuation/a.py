import re


text = "Hello, world. I'm a boy, you're a girl."

replaced = re.sub(r'\S+', lambda m: re.sub(r'^\W+|\W+$', '', m.group()), text)

print(replaced)
