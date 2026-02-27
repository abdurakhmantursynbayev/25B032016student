def fibonacci(n):
    first = 0
    second = 1
    for i in range(n):
        yield first
        x = first + second
        first = second
        second = x
n = int(input())
x = fibonacci(n)
first = True
for i in x:
    if not first:
        print(",", end = "")
    print(i, end ="")
    first = False