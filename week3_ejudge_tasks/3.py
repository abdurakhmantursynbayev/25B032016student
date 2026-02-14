def calc(num, a, b):
    k = 0
    sum1 = 0
    sum2 = 0
    for i in range(0, len(a)):
        if a[i] in b:
            index = i
            command = a[i]
            break
    part1 = a[0: index]
    part2 = a[(index+1):]
    for i in range(0,len(part1),3):
        sum1 *= 10
        sum1 += num[part1[i:(i + 3)]]
    for i in range(0,len(part2),3):
        sum2 *= 10
        sum2 += num[part2[i:(i + 3)]]

    if command == "+":
        summ = sum1 + sum2
    elif command == "-":
        summ = sum1 - sum2
    elif command == "*":
        summ = sum1 * sum2
    summ_in_str = str(summ)
    output = str()
    for i in summ_in_str:
        output += num[int(i)]
    print(output)



num = {
    "ZER":0,"ONE":1,"TWO":2,"THR":3,"FOU":4,"FIV":5,"SIX":6,"SEV":7,"EIG":8,"NIN":9,
    0: "ZER",1: "ONE",2: "TWO",3: "THR",4: "FOU",5: "FIV",6: "SIX",7: "SEV",8: "EIG",9: "NIN"
}
b = ("+", "*", "-")

a = input()
calc(num, a, b)
