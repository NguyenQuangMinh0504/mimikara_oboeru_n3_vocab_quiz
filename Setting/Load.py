import json


class Load:

    @staticmethod
    def load_unit_complete():
        with open("../Data/Status/unit_complete.json") as json_file:
            data = json.load(json_file)
        return data
