import re

with open("raw.txt", "r") as f:
    x = f.read()

pattern = "Стоимость\n(\d+,\d+)"
print(re.findall(pattern, x))