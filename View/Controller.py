from View.Widget.gtts_sound import WordSound


def frame_one(application, new_frame):
    for i, j in application.frame.dict:
        j.config(command=lambda: change_scene(application, new_frame))


def change_scene(application, new_frame):
    application.frame.destroy()
    application.frame = new_frame
    application.frame.pack()


def play_sound(frame):
    frame.sound_btn.config(command=lambda: WordSound.play_word_sound(frame.word))
