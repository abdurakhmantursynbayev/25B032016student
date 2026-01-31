n = int(input())
a = list(map(int, input().split()))
maxx = a[0]
position = 0
for i in range(n):
    if maxx < a[i]:
        maxx = a[i]
        position = i
print(position + 1)
