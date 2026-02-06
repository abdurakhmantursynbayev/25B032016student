n = int(input())
a = []
for i in range(n):
    t = input()
    a.append(t)
b = []
for i in range(n):
    if b.count(a[i]) == 0:
        b.append(a[i])
k = 0;
for i in range(len(b)):
    if a.count(b[i]) == 3:
        k +=1
print(k)