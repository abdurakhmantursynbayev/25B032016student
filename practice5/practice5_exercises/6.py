import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    x = f.read()

it = re.finditer(r"ИТОГО:", x)
x = x[0: next(it).start()]

pattern = r"\d+\.\s*[-,%\[\]\(\)\№\w ]*"
pattern2 = r"(\d+\,\d+) [x] ([\d+]?[ ]?\d+\,\d+)"
matches = re.findall(pattern2, x)
m = re.findall(pattern, x)
for_json = {}
for_json["number"] = []
for_json["product"] = []
for_json["prices"] = []
for_json["QTY"] = []
for_json["price_of_product"] = []

pattern3 = r"Стоимость\s*\d+[ ]?\d+\,\d+"
matchess = re.findall(pattern3, x)

pattern4 = r"(\d+\,\d+) [x] ([\d+]?[ ]?\d+\,\d+)"
prices_and_count = re.findall(pattern4, x)
for i in prices_and_count:
    for_json["QTY"].append(i[0])
    for_json["price_of_product"].append(i[1])


for i in matchess:
    m2 = re.findall(r"\d+[ ]?\d+\,\d+", i)
    for_json["prices"].append(m2[0])
for i in m:
    for_json["number"].append(i[0:3])
    for_json["product"].append(str(i[3:]))

    


json_version = json.dumps(for_json, ensure_ascii=False, indent = 4)
print(json_version)