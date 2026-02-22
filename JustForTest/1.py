def translate(a, strr1, strr2, command):
    sum1 = 0
    sum2 = 0
    for i in range(0,len(strr1), 3):
        g = strr1[(i):(i + 3)]
        print(g)
        sum1 *=10
        sum1 += int(a[g])

    for i in range(0,len(strr2), 3):
        gg = strr2[i:( i+ 3)]
        print(gg)
        sum2 += int(a[gg])
    if command == "+":
        summ = sum1 + sum2
    elif command == "-":
        summ = sum1 - sum2
    elif command == "*":
        summ = sum1 * sum2
    print(summ)
    str_sum = str(summ)
    output = ""
    for i in str_sum:
        output += a[int(i)]
    print(output)



a = {
"ZER":0,"ONE":1,"TWO":2,"THR":3,"FOU":4,"FIV":5,"SIX":6,"SEV":7,"EIG":8,"NIN":9,
    0: "ZER",1: "ONE",2: "TWO",3: "THR",4: "FOU",5: "FIV",6: "SIX",7: "SEV",8: "EIG",9: "NIN"
}

strr = input()
b = ("+", "-", "*")
for i in strr:
    if i in b:
        command = i
        index = strr.find(i)
strr1 = strr[0:index]
strr2 = strr[index + 1:]
print(index, strr)
print(strr1, strr2)
translate(a, strr1, strr2, command)
