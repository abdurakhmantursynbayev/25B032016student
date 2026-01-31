a = int(input())
while a < (2 ** 4):
    a *=2
    print(a, end = " ")
    if a == 2 ** 4:
        break
else:
    print("- it's not equal to 2^4 if multiplies to 2 several times")