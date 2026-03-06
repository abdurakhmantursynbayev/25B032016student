import re
text = "aabbb abbb abbb ab ab abbab ababb  ab ab abb abb a"

pattern = r"a[b]{2,3}"
print(re.findall(pattern, text))