import re

a = input()
pattern = r"\S+@\S+\.\S+"

try:
    print(re.search(pattern, a).group())
except:
    print("No email")