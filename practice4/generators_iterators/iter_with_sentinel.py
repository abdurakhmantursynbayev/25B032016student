import random

random.seed(42)

# Roll a die until we get a 6
rolls = iter(lambda: random.randint(1, 3), 2)
print(list(rolls))