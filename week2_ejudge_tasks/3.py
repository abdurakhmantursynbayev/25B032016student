n = int(input())
a = list(map(int, input().split()))
summ = 0
for i in range(n):
    summ += a[i]
print(summ)