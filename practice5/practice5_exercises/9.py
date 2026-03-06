import re

text = "ThisIsATestStringForPythonProgrammingAndRegexPractice"

result = re.sub(r'(?<!^)([A-Z])', r' \1', text)

print(result)