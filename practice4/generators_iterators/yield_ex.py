def str_generator(my_str):
    x = 0
    while x < len(my_str):
        yield my_str[x]
        x += 1
a = str_generator("abdurakhman")
for i in a:
    print(i, end=" ")