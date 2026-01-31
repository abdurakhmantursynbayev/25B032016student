a = 10
b = 16 
c = 4
if a * b < c:
    print(a * b)
elif a * c < b:
    print(a * c)     #after using "if" we can use elif as much as we want
elif b * c < a:
    print(b * c)     #in the end if all of this condition is false we can use else it will work in any other conditions
else:
    print(a, b, c)
    