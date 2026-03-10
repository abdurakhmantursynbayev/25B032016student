import os

with os.scandir('.') as all:
    for i in all:
        if i.is_file() and i.name.endswith('.py'):
            print(f"file: {i.name}")