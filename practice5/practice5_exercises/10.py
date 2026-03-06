import re

def camel_to_snake(text):
    snake = re.sub(r'([a-z])([A-Z])', r'\1_\2', text)
    return snake.lower()

s = input()
print(camel_to_snake(s))