def generator():
    yield 1
    yield 2
    yield 3
a = generator()
print(next(a))
print(next(a))
print(next(a))
a = generator()
for i in a:
    print(i)

#  The yield keyword is what makes a function a generator.

#  When yield is encountered,
#  the function's state is saved,
#  and the value is returned.
#  The next time the generator is called,
#  it continues from where it left off.

