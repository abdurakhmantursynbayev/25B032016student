command, *others = map(str, input().split())
if command == "set":
    key, value = others.split()
else:
    key = others[0]
print(command, key)