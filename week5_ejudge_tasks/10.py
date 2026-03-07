import re
a = input()
try:
    re.search(r"cat|dog", a).group()
    print("Yes")

except:
    print("No")
