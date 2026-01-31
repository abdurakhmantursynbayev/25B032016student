a = 10
b = 20
if a < b: print(b)

print("A") if a > b else print("B")

c = a ** 2 if a ** 2 > b else b
print(c)

print("1condition") if a > b else print("none") if a * 2 == b else print("third condition")