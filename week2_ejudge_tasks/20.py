n = int(input())
a = {}
for i in range(n):
    command, *others= map(str, input().split())
    if command == "set":
        key = others[0]
        value = others[1]
        a[key] = value
    elif command == "get":
        key = others[0]
        if key in a:
            print(a[key])
        else:
            print(f"KE: no key {key} found in the document")