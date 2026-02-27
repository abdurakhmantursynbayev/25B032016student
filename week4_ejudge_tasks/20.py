command_n = int(input())
g = 0; n = 0
for i in range(command_n):
    command, x = map(str, input().split())
    x = int(x)
    if command == "global":
        g += x
    elif command == "nonlocal":
        n += x
print(g, n)