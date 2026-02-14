n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    command, *number = map(str, input().split())
    if command == "abs":
        a = list(map(lambda x: abs(x), a))
    elif command == "add":
        a = list(map(lambda x: x + int(number[0]), a))
    elif command == "multiply":
        a = list(map(lambda x: x * int(number[0]), a))
    elif command == "power":
        a = list(map(lambda x: x ** int(number[0]), a))
for x in a:
    print(x, end=" ")