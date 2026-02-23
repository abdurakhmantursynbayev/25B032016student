from itertools import islice

class counter_numbers:
    def __init__(self, start = 0, step = 1):
        self.current = start
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        x = self.current
        self.current += self.step
        return x
x = counter_numbers(0, 5)
list_of_numbers = list(islice(x, 5))
print(list_of_numbers)