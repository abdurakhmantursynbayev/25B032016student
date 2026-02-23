n = int(input())
class even_numbers:
    def __init__(self):
        self.n = n
        self.start = 0
    def __iter__(self):
        return self
    def __next__(self):
        x = self.start
        if x >= n:
            raise StopIteration
        self.start += 2
        return x
x = even_numbers()
myit = iter(x)
for i in myit:
    print(i, end = ", ")