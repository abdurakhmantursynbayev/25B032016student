def div(n):
    for i in range(0, n + 1, 12):
        yield i
n = int(input())
x = div(n)
first = True
for i in x:
    if not first:
        print(" ", end ="")
    print(i, end ="")
    first = False