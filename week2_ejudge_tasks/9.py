len_ = int(input())
a = list(map(int, input().split()))
min_ = min(a)
max_ = max(a)
for i in range(len_):
    if a[i] == max_:
        a[i] = min_
for x in a:
    print(x, end = " ")