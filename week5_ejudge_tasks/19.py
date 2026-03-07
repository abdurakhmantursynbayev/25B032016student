import re

a = input()
pattern = re.compile(r"\w+")
x = a.split(" ")
s = 0
for i in x:
    if pattern.match(i):
        s +=1
print(s)