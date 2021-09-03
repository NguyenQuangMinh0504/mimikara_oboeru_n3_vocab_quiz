from gtts import gTTS
import os
from View.Widget.Sound import Sound


class WordSound:

    @staticmethod
    def play_word_sound(word):
        language = 'ja'
        try:
            word_sound = gTTS(text=word, lang=language, slow=False)
            word_sound.save("word_sound.wav")
            Sound.play_sound("word_sound.wav")
            os.remove('word_sound.wav')
        except AssertionError:
            pass
