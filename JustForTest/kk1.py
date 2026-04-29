a, b ,c = map(int, input().split())
s = ""
array = []
array.append(a)
array.append(b)
array.append(c)
array.sort()
array.reverse()
s = ""
s += str(array[0])
s += str(array[1])
s += str(array[2])
print(int(s))
