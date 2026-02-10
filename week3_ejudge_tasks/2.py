def is_it_usual(n):
    while n > 1:
        if n % 2 == 0:
            n /=2
        if n % 3 == 0:
            n /= 3
        if n % 5 == 0:
            n /= 5
        if n % 5 != 0 and n % 2 != 0 and n % 3 != 0 and n > 1:
            return "No"
    else:
        return "Yes"
    

n = int(input())
a = is_it_usual(n)
print(a)