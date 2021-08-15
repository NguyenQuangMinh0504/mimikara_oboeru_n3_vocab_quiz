import json

with open("../Data/Status/unit_complete.json") as json_file:
    data = json.load(json_file)
print(data)
