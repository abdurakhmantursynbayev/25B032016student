import json

def differences(a, b, printed, c =""):
    for key, value in b.items():
        if key not in a:
            print(f"{c}{key} : {a[key]} -> {value}")
        if type(value) != dict and a[key] != value:
            print(f"{c}{key} : {a[key]} -> {value}")
            printed = True
        elif type(value) == dict:
            c += str(key) + "."
            printed = differences(a[key], value, printed, c)
    return printed


first = input()
second = input()
dictf = json.loads(first)
first = json.dumps(dictf, sort_keys=True)
dictf = json.loads(first)
dicts = json.loads(second)
second = json.dumps(dicts, sort_keys= True)
dicts = json.loads(second)
printed = False
x = differences(dictf, dicts, printed, c = "")
if not x:
    print("No differences")