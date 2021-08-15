import json
with open("../Data/Status/unit_complete.json", 'w') as outfile:
    data = {"Unit 1": False, "Unit 2": False, "Unit 3": False, "Unit 4": False, "Unit 5": False, "Unit 6": False,
            "Unit 7": False, "Unit 8": False, "Unit 9": False, "Unit 10": False, "Unit 11": False, "Unit 12": False}
    json.dump(data, outfile)
