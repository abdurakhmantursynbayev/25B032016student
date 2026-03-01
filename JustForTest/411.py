import json

a = input()
b = input()
a_dict = json.loads(a)
b_dict = json.loads(b)
def mfun(a_dict, b_dict):
    for key, value in b_dict.items():
        if value == None and key in a_dict:
            del a_dict[key]
        elif key in a_dict and type(value) != dict:
            a_dict[key] = value
        elif key in a_dict and type(value) == dict:
            mfun(a_dict[key], value)
        elif key not in a_dict:
            a_dict[key] = value

mfun(a_dict, b_dict)
output = json.dumps(a_dict, sort_keys=True)
print(output)