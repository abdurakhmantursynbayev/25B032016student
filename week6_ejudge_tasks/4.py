n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0
for i, j in zip(a, b):
    sum += i * j
print(sum)