import re
a = input()

print(len(re.findall(r"\w+", a)))