import re

a = input()
x = re.findall(r"\d{2,}", a)
for i in x:
    if i is x[-1]:
        print(i)
    else:
        print(i, end =" ")