import re

a = input()

pattern = "Name: ([ '\w]+), Age: (\d+)"
print(re.search(pattern, a).group(1), re.search(pattern, a).group(2))