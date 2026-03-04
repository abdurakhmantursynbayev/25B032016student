import re

with open("raw.txt", "r") as f:
    x = f.read()
pattern = r"Стоимость\s*\d+[ ]?\d+\,\d+"
matches = re.findall(pattern, x)
for i in matches:
    m = re.findall(r"\d+[ ]?\d+\,\d+", i)
    print(f"Price: {m[0]}")
f.close()