n = int(input())
def squares(n):
    for i in range(n + 1):
        yield i * i
x = squares(n)
for i in x:
    print(i)