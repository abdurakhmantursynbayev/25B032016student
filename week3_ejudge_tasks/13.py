from math import sqrt
a = list(map(int, input().split()))

b = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(sqrt(x) + 1))), a))
if len(b) == 0:
    print("No primes")
else:
    for x in b:
        print(x, end = " ")