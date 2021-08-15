import json
import pandas as pd


def load_unit_complete():

    with open("../Data/Status/unit_complete.json") as json_file:
        data = json.load(json_file)
    return data


def load_data(file):
    try:
        path = '../mimikara_oboeru_n3_vocab_quiz/Data/Dictionary/'
        return pd.read_csv(path+file)
    except FileExistsError:
        print("File not found")
