import re

a = input()

if re.match(r"^\w.*\d$", a):
    print("Yes")
else:
    print("No")