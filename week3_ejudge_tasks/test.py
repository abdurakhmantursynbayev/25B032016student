class name_of_class:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def getin(self):
        self.a, self.b = map(int, input().split())
    def hello(self):
        print("hello 1")
class something_nothing(name_of_class):
    def __init__(self, a, b, name, surname):
        super().__init__(a, b)
        self.name = name
        self.surn = surname
    def hello(self):
        print("hello 2")
a = something_nothing(2, 5, "abdu", "bu")
a.hello()
print(a.a, a.b)
print(a.name, a.surn)