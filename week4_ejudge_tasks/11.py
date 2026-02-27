import json


def json_into_dict(output, json_patch):
    for key, value in json_patch.items():
        if type(value) == dict and key in output:
            if type(output[key]) == dict:
                json_into_dict(output[key], value)
            else:
                output[key] = value
        elif type(value) == dict and key not in output:
            output[key] = value
            json_into_dict(output[key], value)
        elif value is None:
            output.pop(key, None)
            continue
        else:
            output[key] = value
        

json_source = input()
source = json.loads(json_source)
json_patch = input()
patch = json.loads(json_patch)
output = source
json_into_dict(output, patch)
json_string = json.dumps(output, sort_keys=True, separators = (',', ':'))
print(json_string)