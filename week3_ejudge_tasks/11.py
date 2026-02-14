class pair:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.a1 = 0
        self.b1 = 0
    def getinnf(self):
        self.a, self.b, self.a1, self.b1 = map(int,input().split())

class adding(pair):
    def __init__(self):
        super().__init__()
    def addpair(self):
        sum_a = self.a + self.a1
        sum_b = self.b + self.b1
        print(f"Result: {sum_a} {sum_b}")
x = adding()
x.getinnf()
x.addpair()
