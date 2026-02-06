n = int(input())
a = {}
for i in range(n):
    st, nn = map(str, input().split())
    nn = int(nn)
    if st in a:
        a[st] += nn
    else:
        a[st] = nn
sorted_d = dict(sorted(a.items()))
for x in sorted_d:
    print(x, sorted_d[x])