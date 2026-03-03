import re
text = "-55 -27 -46 -2 -1 +23 +38"
pattern = r'([+-]?\d+\b)\s([+-]?\d+\b)\s.(\d+)'
match = re.search(pattern, text)
print(match.group())