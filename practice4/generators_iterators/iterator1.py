a = [1, 2, 3, 4, 5]
b = iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))


#for string we also can use iterators

mystr = "hello world"
myit_for_str = iter(mystr)
print(next(myit_for_str))
print(next(myit_for_str))
print(next(myit_for_str))
print(next(myit_for_str))
