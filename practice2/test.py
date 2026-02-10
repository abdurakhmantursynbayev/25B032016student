n = int(input())
a = map(int, input().split())
b = {}

for x in a:
    if x in b:
        b[x] +=1
    else:
        b[x] = 1
sorted_d = dict(sorted(b.items()))
maxx = 0
element = 0
for x in sorted_d:
    if sorted_d[x] > maxx:
        maxx = sorted_d[x]
        element = x
print(element)
