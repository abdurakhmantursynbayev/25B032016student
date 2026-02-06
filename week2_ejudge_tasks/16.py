n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if b.count(a[i]) == 0:
        b.append(a[i])
        print("YES")
    else:
        print("NO")