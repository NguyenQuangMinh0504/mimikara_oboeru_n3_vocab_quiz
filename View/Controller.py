from View.Widget.Frame import QuizFrame
from View.Widget.gtts_sound import WordSound
from View import Model



def frame_one(frame):
    for i, j in frame.dict:
        j.config(command=lambda: change_scene(frame.parent, i))


def change_scene(application, i):
    application.frame.destroy()
    new_frame = QuizFrame(application, i)
    application.frame = new_frame
    application.frame.pack()


def play_sound(frame):
    frame.sound_btn.config(command=lambda: WordSound.play_word_sound(frame.word))


def button_validate(frame):
    frame.label_input_frame.spelling_input.config(validate='all',
                                                  validatecommand=frame.parent.register(lambda: validate(frame.parent)))


def validate(application):
    # if action == '0':  # currently has a bug for font
    #     self.input_frame.kanji_input.delete(0, tk.END)

    application.frame.status['text'] = ''
    application.frame.meaning['text'] = ''
    application.frame.spelling['text'] = ''
    application.frame.kanji['text'] = ''

    return True
