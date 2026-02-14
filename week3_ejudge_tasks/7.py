from math import sqrt
class point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def getin(self):
        self.x, self.y = map(int, input().split())
    def show(self):
        print(f"({self.x}, {self.y})")
    def moves(self, x1, y1):
        self.x = x1
        self.y = y1
    def dist(self, x2, y2):
        dstnce = sqrt(abs(x2-self.x) ** 2 + abs(y2 - self.y) ** 2)
        print(f"{dstnce:.2f}")
first = point()
second = point()
third = point()
first.getin()
second.getin()
third.getin()
first.show()
second.show()
first.moves(second.x, second.y)
first.dist(third.x, third.y)