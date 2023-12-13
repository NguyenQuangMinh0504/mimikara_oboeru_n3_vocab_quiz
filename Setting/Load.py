import json
import pandas as pd
import sys
import os

unit_complete_path = "Data/Status/unit_complete.json"
user_status_path = "Data/Status/user_status.txt"
sound_setting_path = "Data/Status/sound_setting.json"


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """

    # Problems
    # https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


right_sound_path = resource_path("Assets/Sound/right_sound.wav")
wrong_sound_path = resource_path("Assets/Sound/wrong_sound.wav")
logo_path = resource_path("Assets/Image/app_icon-2.gif")
sound_button_path = resource_path("Assets/Image/50px_sound_button.gif")


def get_unit_complete():
    with open(resource_path(unit_complete_path)) as json_file:
        return json.load(json_file)


def set_unit_complete(data):
    with open(resource_path(unit_complete_path), 'w') as json_file:
        json.dump(data, json_file)


def load_data(file) -> pd.DataFrame:
    """
    Loading unit vocabulary from unit.csv file"""
    try:
        path = resource_path("Data/Dictionary/") + file + ".csv"
        return pd.read_csv(path)
    except FileNotFoundError:
        print(path)
        print(sys.path)
        print("File not found")


def add_active_day(day):
    with open(resource_path(user_status_path), 'a') as f:
        f.write('\n' + day)


def get_active_day():
    with open(resource_path(user_status_path), 'r') as f:
        return [i.rstrip() for i in f.readlines()]


def get_sound_setting():
    with open(resource_path(sound_setting_path), 'r') as json_file:
        return json.load(json_file)


def set_sound_setting(data):
    with open(resource_path(sound_setting_path), 'w') as json_file:
        json.dump(data, json_file)
