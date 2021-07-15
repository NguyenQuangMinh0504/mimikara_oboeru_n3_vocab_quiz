from gtts import gTTS
import os


class WordSound:

    @staticmethod
    def play_word_sound(word):
        language = 'ja'
        if '＜他＞' in word:
            word = word.replace('＜他＞', '')
        if '＜自＞' in word:
            word = word.replace('＜自＞', '')
        try:
            word_sound = gTTS(text=word, lang=language, slow=False)
            word_sound.save("word_sound.wav")
            os.system("afplay word_sound.wav")
            os.remove('word_sound.wav')
        except AssertionError:
            pass
