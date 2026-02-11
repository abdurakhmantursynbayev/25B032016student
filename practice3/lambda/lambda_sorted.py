n = int(input())
s = list(map(int, input().split()))
a = {}
for x in s:
    if x in a:
        a[x] += 1
    else:
        a[x] = 1
sorted_d = dict(sorted(a.items(), key = lambda x: (x[1], -x[0]), reverse= True))
for i in sorted_d:
    print(i)