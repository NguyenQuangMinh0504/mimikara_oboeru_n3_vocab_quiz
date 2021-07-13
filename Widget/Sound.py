import os


class Sound:
    @ staticmethod
    def play_right_sound():
        path = './Data/Sound/right_sound.wav'
        os.system("afplay " + path)

    @staticmethod
    def play_wrong_sould():
        path = './Data/Sound/wrong_sound.wav'
        os.system("afplay " + path)
