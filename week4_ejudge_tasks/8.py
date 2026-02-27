import math
n = int(input())
def prime_numbers(n):
    for i in range(2, n + 1):
        prime = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                prime = False
        if prime:
            yield i

x = prime_numbers(n)
first = True
for i in x:
    if not first:
        print(" ", end = "")
    print(i, end = "")
    first = False