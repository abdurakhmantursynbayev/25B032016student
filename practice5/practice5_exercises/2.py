import re

with open("raw.txt", "r") as f:
    x = f.read()
it = re.finditer(r"ИТОГО:", x)
x = x[0: next(it).start()]

pattern = r"\d+\.\s*[-,%\[\]\(\)\№\w ]*"
m = re.findall(pattern, x)
for i in m:
    print(i)
f.close()