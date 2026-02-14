class person:
    def __init__(self):
        self.name = ""

class student(person):
    def __init__(self):
        super().__init__()
        self.gpa = 0
    def getinf(self):
        self.name, self.gpa = map(str, input().split())
        self.gpa = float(self.gpa)
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

x = student()
x.getinf()
x.display()
