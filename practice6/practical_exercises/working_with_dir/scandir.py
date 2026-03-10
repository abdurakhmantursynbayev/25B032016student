import os

with os.scandir('.') as entries:
    for entry in entries:
        if entry.is_file():
            print(f'File: {entry.name}')
        elif entry.is_dir():
            print(f'Dir:  {entry.name}')