n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
for x in a:
    print(x, end = " ")