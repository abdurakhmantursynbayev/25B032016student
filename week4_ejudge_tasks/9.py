def two_powers(n):
    for i in range(0, n + 1):
        yield pow(2, i)

n = int(input())
x = two_powers(n)
first = True
for i in x:
    if not first:
        print(" ", end = "")
    print(i, end = "")
    first = False