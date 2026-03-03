import re
text = "Phone: +7-777-123-45-67, backup: +7-701-987-65-43"
match = re.findall(r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", text)
print(match)
