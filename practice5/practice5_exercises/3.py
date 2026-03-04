import re

def mf(x, y):
    x = x.replace(" ", "").replace(",", ".")
    y = y.replace(" ", "").replace(",", ".")
    return float(x) * float(y)


with open("raw.txt", "r") as f:
    x = f.read()

pattern = r"(\d+\,\d+) [x] ([\d+]?[ ]?\d+\,\d+)"
matches = re.findall(pattern, x)
sum = 0

for i in matches:
    # mf(str(i[0]), str(i[1]))
    sum += mf(str(i[0]), str(i[1]))
print(sum)

f.close()