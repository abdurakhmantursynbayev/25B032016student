class shape:
    def __init__(self):
        self.length = 0

    def getlen(self):
        self.length = int(input())

class area(shape):
    def __init__(self):
        super().__init__()
    def printarea(self):
        print(self.length ** 2)

x = area()
x.getlen()
x.printarea()