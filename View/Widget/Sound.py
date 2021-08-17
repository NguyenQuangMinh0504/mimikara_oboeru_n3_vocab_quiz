import os
from platform import system


class Sound:
    @ staticmethod
    def play_right_sound():
        path = '../Assets/Sound/right_sound.wav'
        Sound.play_sound(path)

    @staticmethod
    def play_wrong_sound():
        path = '../Assets/Sound/wrong_sound.wav'
        Sound.play_sound(path)

    @staticmethod
    def play_sound(path):
        sys = system()
        if sys == 'Windows':
            import winsound
            winsound.PlaySound(path, winsound.SND_FILENAME)
        elif sys == 'Darwin':
            os.system("afplay " + path)
