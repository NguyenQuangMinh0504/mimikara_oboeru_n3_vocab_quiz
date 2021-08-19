import os
from platform import system

import Setting.Load


class Sound:
    @ staticmethod
    def play_right_sound():
        Sound.play_sound(Setting.Load.right_sound_path)

    @staticmethod
    def play_wrong_sound():
        Sound.play_sound(Setting.Load.wrong_sound_path)

    @staticmethod
    def play_sound(path):
        sys = system()
        if sys == 'Windows':
            import winsound
            winsound.PlaySound(path, winsound.SND_FILENAME)
        elif sys == 'Darwin':
            os.system("afplay " + path)
