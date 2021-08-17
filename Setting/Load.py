import json
import pandas as pd
import sys


def get_unit_complete():

    with open("./Data/Status/unit_complete.json") as json_file:
        data = json.load(json_file)
    return data


def set_unit_complete(data):
    with open("./Data/Status/unit_complete.json", 'w') as json_file:
        json.dump(data, json_file)


def load_data(file):
    try:
        path = './Data/Dictionary/'
        return pd.read_csv(path+file+'.csv')
    except FileNotFoundError:
        print(sys.path)
        print("File not found")


def add_active_day(day):
    with open('./Data/Status/user_status.txt', 'a') as f:
        f.write('\n' + day)


def get_active_day():
    with open('./Data/Status/user_status.txt', 'r') as f:
        return [i.rstrip() for i in f.readlines()]