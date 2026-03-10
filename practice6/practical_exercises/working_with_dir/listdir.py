import os

BASE = os.getcwd()

for name in os.listdir(BASE):
    full_path = os.path.join(BASE, name)
    if os.path.isfile(full_path):
        print(f'FILE: {name}')
    else:
        print(f' DIR: {name}')