import re 

x = input()

if re.match(r"Hello", x):
    print("Yes")
else:
    print("No")