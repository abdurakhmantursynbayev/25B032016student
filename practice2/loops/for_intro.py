n = int(input())
for i in range(n):
    print(i, end = " ")
print()
for x in "abdurakhman":
    print(x, end =" ")
    if x == "u":
        break
    elif x == "d":
        continue
    print("-", end = " ")