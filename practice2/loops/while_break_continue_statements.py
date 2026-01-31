a = "abdurakhman"
k =-1
while k < len(a):
    k +=1
    if a[k] == "a":
        continue
    print(a[k], k, end = "   ")
    if a[k] == "m":
        break