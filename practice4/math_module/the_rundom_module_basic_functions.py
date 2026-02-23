import random

# Random float between 0.0 and 1.0
print(random.random())          # e.g., 0.7134

# Random float in a range
print(random.uniform(1.5, 9.5)) # e.g., 6.234

# Random integer in a range (inclusive)
print(random.randint(1, 100))   # e.g., 42

# Random integer in a range (exclusive end), with optional step
print(random.randrange(0, 100, 5))  # e.g., 35 (multiples of 5)



#  Working with Sequences



fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Pick a random element
print(random.choice(fruits))     # e.g., "cherry"

# Pick multiple random elements (with replacement)
print(random.choices(fruits, k=3))  # e.g., ["apple", "date", "apple"]

# Pick multiple random elements (without replacement)
print(random.sample(fruits, k=3))   # e.g., ["banana", "date", "cherry"]

# Shuffle a list in place
random.shuffle(fruits)
print(fruits)  # e.g., ["date", "cherry", "apple", "elderberry", "banana"]