import re

a = input()
pattern = r"\d{2}/\d{2}/\d{4}"
print(len(re.findall(pattern, a)))