import json 
a = {
    "first": 1,
    "second": 2,
    "apple" : "aa"

}

json_string = json.dumps(a, sort_keys = True, indent = 2)
print(json_string)