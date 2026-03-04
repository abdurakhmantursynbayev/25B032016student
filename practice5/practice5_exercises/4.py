import re

with open("raw.txt", "r") as f:
    x = f.read()

pattern_of_date = r"\d{2}\.\d{2}\.\d{4}"
pattern_of_time = r"\d{2}:\d{2}:\d{2}"
print(re.findall(pattern_of_date, x)[0], re.findall(pattern_of_time, x)[0])

f.close()