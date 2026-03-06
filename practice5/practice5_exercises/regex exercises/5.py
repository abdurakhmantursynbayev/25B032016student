import re

text = "In the lab we tested several patterns such as ab, acb, a123b, a_test_b, and aXYZb. However, words like apple, about, and alphabet do not match the rule."

pattern = r"\ba[\S]*b\b"
print(re.findall(pattern, text))