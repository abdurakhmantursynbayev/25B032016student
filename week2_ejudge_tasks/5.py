n = int(input())
a = 1
while a < n:
    a *= 2
    if a == n:
        print("YES")
        break
else:
    print("NO")
