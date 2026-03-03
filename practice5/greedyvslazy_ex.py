import re

html = "<b>bold</b> and <i>italic</i>"

# Greedy — matches everything between first < and last >
print(re.findall(r"^<.*>$", html))
# ['<b>bold</b> and <i>italic</i>']

# Lazy — matches the shortest possible string
print(re.findall(r"<[/]?.>", html))
# ['<b>', '</b>', '<i>', '</i>']