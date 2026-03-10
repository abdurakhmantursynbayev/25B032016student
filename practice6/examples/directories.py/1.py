import os
output = os.path.join("newdir", "nesteddir")
os.makedirs(output, exist_ok = True)

with os.scandir('.') as all:
    for i in all:
        if i.is_file():
            print(f"file: {i.name}")
        else:
            print(f"dir: {i.name}")