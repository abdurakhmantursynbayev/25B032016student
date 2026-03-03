import re

text = "Alice went to Almaty. she met Bob and carol there."


pattern = r"\b[A-Z]\w*\b"
print(re.findall(pattern, text))