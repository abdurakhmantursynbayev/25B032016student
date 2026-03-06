import re

text = "Alice went to Paris with Robert and Maria. They met Daniel near the River and talked about London, Python, and Music. Later, George and Anna joined them for Dinner."

pattern = r"[A-Z]{1}[a-z]+"
print(re.findall(pattern, text))