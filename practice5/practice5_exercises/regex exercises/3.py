import re

text = "hello_world this_is a test_string with python_code and Data_Science but not THIS_TEST"

pattern = r"[_a-z]+"
print(re.findall(pattern, text))
