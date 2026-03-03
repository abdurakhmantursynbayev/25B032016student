import re

def is_error_message(text):
    return bool(re.match(r"^Error.*!$", text))

print(is_error_message("Error: file not found!"))  # True
print(is_error_message("Error: connection lost"))  # False
print(is_error_message("Warning: disk full!")) 