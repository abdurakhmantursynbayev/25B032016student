import re

with open("raw.txt", "r") as f:
    x = f.read()

pattern = r"[: \w]+\s*[, \d]+\s*ИТОГО:"
match = re.findall(pattern, x)[0]
print(re.findall(r"[ \w]+:", match)[0])

f.close()