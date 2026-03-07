import re
a = input()
print(len(re.findall(r"\b\w{3}\b", a)))