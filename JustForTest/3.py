import re

text = input()
pattern = r"\b\w{3}\b"
print(re.findall(pattern, text))