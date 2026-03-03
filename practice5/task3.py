import re

def check_password(password):
    if len(password) >= 8 and bool(re.search(r"\d", password)):
        return "Valid"
    else:
        return "Invalid"
        

print(check_password("abc123"))       # Invalid (too short)
print(check_password("abcdefgh"))     # Invalid (no digit)
print(check_password("abcdef12"))     # Valid