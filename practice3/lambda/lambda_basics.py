#syntax of lambda function ->     lambda arguments:expresesion 

x = lambda a: a ** 2
print(x(5))


# new example:

def funct1(n):
    return lambda a: a * n
total = funct1(5)
print(total(7))