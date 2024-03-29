import json
import pandas as pd
import sys

right_sound_path = './Assets/Sound/right_sound.wav'
wrong_sound_path = './Assets/Sound/wrong_sound.wav'
logo_path = "./Assets/Image/app_icon-2.gif"
sound_button_path = "./Assets/Image/50px_sound_button.gif"


def get_unit_complete():
    with open("./Data/Status/unit_complete.json") as json_file:
        return json.load(json_file)


def set_unit_complete(data):
    with open("./Data/Status/unit_complete.json", 'w') as json_file:
        json.dump(data, json_file)


def load_data(file) -> pd.DataFrame:
    """
    Loading unit vocabulary from unit.csv file"""
    try:
        path = './Data/Dictionary/'
        return pd.read_csv(path + file + '.csv')
    except FileNotFoundError:
        print(sys.path)
        print("File not found")


def add_active_day(day):
    with open('./Data/Status/user_status.txt', 'a') as f:
        f.write('\n' + day)


def get_active_day():
    with open('./Data/Status/user_status.txt', 'r') as f:
        return [i.rstrip() for i in f.readlines()]


def get_sound_setting():
    with open("./Data/Status/sound_setting.json", 'r') as json_file:
        return json.load(json_file)


def set_sound_setting(data):
    with open("./Data/Status/sound_setting.json", 'w') as json_file:
        json.dump(data, json_file)
