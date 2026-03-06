import re

s = input()
p = input()
r = input()

s = re.sub(p, r, s)
print(s)