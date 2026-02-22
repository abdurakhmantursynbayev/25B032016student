class the_string:
    def __init__(self):
        self.str = "abdurakhman"
        self.i = 0
    def getin(self):
        self.str = input()
    def __iter__(self):
        return self
    def __next__(self):
        x = self.i
        self.i += 1
        return self.str[x]

new = the_string()
new.getin()
b = iter(new)
print(next(new))
print(next(new))    
print(next(new))    
print(next(new))    
print(next(new))


