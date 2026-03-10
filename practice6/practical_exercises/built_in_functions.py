s = "abdurakhman"
output = list(map(lambda x: x + " ", s))
print(output)
result = ""
for i in output:
    result += i
print(result)


#filter
a = [1, 2, 3, 4, 5, 6, 7]
even_numbers = list(filter(lambda x: x % 2 == 0, a))
print(even_numbers)

#enumerate

students = ["abdurakhman", "erasyl", "esymkhan", "ersultan", "beksultan", "spider-man"]

for i, name in enumerate(students, start = 1):
    print(f"id: {i} name: {name}")

#zip

scores = ["100", "99", "71", "85", "89,5"]
student_names = ["abdu", "spider-man", "superman", "luffy"]
for i, j in zip(scores, student_names):
    print(f"id: {i}, name: {j}")

