def funct(n):
    t = True
    for x in n:
        if int(x) % 2 != 0:
            t = False
    return t
        



n = input()
t = funct(n)
if t:
    print("Valid")
else:
    print("Not valid")

