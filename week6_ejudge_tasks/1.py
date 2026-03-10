n = int(input())
s = list(map(int, input().split()))
result = list(map(lambda x: x * x, s))
print(sum(result))