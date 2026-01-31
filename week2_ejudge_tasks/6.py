n = int(input())
a = list(map(int, input().split()))
maxx = a[0]
for i in range(n):
    if maxx < a[i]:
        maxx = a[i]
print(maxx)