import json
import pandas as pd
import sys


def load_unit_complete():

    with open("../Data/Status/unit_complete.json") as json_file:
        data = json.load(json_file)
    return data


def load_data(file):
    try:
        path = '../Data/Dictionary/'
        return pd.read_csv(path+file+'.csv')
    except FileNotFoundError:
        print(sys.path)
        print("File not found")
