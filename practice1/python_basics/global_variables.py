def funct():
    global x
    x = 5
    print(x)

x = 7
print(x)
funct()
print(x)