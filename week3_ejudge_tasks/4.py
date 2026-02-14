class StringHandler:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printstr(self):
        print(self.s.upper())

obj = StringHandler()
obj.getString()
obj.printstr()
