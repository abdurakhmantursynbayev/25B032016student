import re

text = "Hello, my name is Alex. I study Python, data science, and mathematics. Today I solved many problems, wrote some code, and learned regex."
pattern = r"[. ,]"
x = re.findall(pattern, text)
for i in x:
    text = text.replace(i, ":")
print(text)