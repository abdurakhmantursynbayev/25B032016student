"""gen_exp = (i * i for i in range(6))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
a = "abdurakhman gvybunoipmoioiuyutycrtvybu"
print(a[next(gen_exp)])
print(a[next(gen_exp)])
"""

def echo_generator():
  while True:
    received = yield
    sending = yield
    print("Received:", received, end =" ")
    print(sending)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")   # for first yield "received"
gen.send("World")  # for second yield "sending"
gen.send("first")  # starts from "received" because there are no more yield than 2
gen.send("second")