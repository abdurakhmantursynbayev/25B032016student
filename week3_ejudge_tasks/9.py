class Circle:
    def __init__(self):
        self.pi = 3.14159
        self.r = 0
    def getr(self):
        self.r = int(input())
    def area(self):
        x = self.r * self.r * self.pi
        print(f"{x:.2f}")
x = Circle()
x.getr()
x.area()
