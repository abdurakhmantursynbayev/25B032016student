class reverse:
    def __init__(self, obj):
        self.obj = obj
        self.back = len(self.obj) - 1
        self.front = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.back < self.front:
            raise StopIteration
        x = self.obj[self.back]
        self.back -= 1
        return x
strr = input()
x = reverse(strr)
myit = iter(x)
for i in myit:
    print(i, end ="")
