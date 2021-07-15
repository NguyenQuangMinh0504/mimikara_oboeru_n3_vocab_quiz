import os


class Sound:
    @ staticmethod
    def play_right_sound():
        path = './Assets/Sound/right_sound.wav'
        os.system("afplay " + path)

    @staticmethod
    def play_wrong_sould():
        path = './Assets/Sound/wrong_sound.wav'
        os.system("afplay " + path)
