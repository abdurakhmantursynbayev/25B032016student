def k_times(a, k):
    for _ in range(k):
        yield a

a = list(map(str, input().split()))
k = int(input())
x = k_times(a, k)
first = True
for i in x:
    for j in i:
        if not first:
            print(" ", end = "")
        print(j, end = "")
        first = False