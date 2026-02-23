import json
json_string = '{"name": "Askar", "age": 25, "courses": ["PP2", "Algorithms"]}'

dict_a = json.loads(json_string)
print(dict_a)