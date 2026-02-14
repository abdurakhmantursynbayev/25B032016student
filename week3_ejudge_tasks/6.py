class shape:
    def __init__(self):
        self.length = 0
        self.width = 0
    def getlw(self):
        self.length, self.width = map(int, input().split())
class area(shape):
    def __init__(self):
        super().__init__()
    def printout(self):
        print(self.length * self.width)
x = area()
x.getlw()
x.printout()