import re

s = input()
p = input()

x = re.split(p, s)
for i in range(len(x)):
    if i + 1 == len(x):
        print(x[i])
    else:
        print(x[i], end = ",")