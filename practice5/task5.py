import re

def validate_email(email):
    pattern = re.match(r"^[\w.-]+@[\w.-]+\.\w{2,4}", email)
    return bool(pattern)

print(validate_email("student@kbtu.kz"))    # True
print(validate_email("user.name@mail.com")) # True
print(validate_email("bad@email"))          # False
print(validate_email("@nodomain.com"))      # False
