import re

text = input()

def double_digit(match):
    d = match.group()
    return d * 2

result = re.sub(r'\d', double_digit, text)

print(result)