import re

a = input()

x = re.findall(r"\d", a)

for i in range(len(x)):
    if i + 1 == len(x):
        print(x[i])
        break
    print(x[i], end= " ")