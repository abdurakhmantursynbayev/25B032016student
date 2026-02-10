def difference(a, b):
    print(a - b)
a, b = map(int, input().split())
difference(a, b)

# second function:

def funct1(name,age, animal = "cat",):
    print(name , " has" )
    print(f"age of {name}", age)
funct1("Alex", age = 19, animal = "dog")