n, l, r = map(int, input().split())
a = list(map(int, input().split()))
l -=1;r -=1
while l < r:
    t = a[l]
    a[l] = a[r]
    a[r] = t
    l+=1; r-=1

for x in a:
    print(x, end = " ")