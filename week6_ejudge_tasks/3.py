n = int(input())
s = list(map(str, input().split()))
for i, word in enumerate(s):
    if i == len(s) - 1:
        print(f"{i}:{word}")
    else:
        print(f"{i}:{word}", end = " ")