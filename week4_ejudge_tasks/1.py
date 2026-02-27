def squares(n):
    for i in range(1, n + 1):
        yield i * i

n = int(input())
x = squares(n)
for i in x:
    print(i)