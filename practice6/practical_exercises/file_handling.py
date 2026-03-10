# 'r'	Read (default). Error if file doesn't exist
# 'w'	Write. Creates file or overwrites existing
# 'a'	Append. Creates file or adds to the end
# 'x'	Create. Error if file already exists

f = open("input.txt", "w")
f.write("Hello world\n")
f.write("Hello Abdurakhman\n")
f.close()

f = open("input.txt","r")
output = f.read()
print(output)
f.close()

with open("input.txt", "r") as f:
    print(f.readline())
    print(f.readline())
