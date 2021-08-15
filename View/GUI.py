import random
import pandas as pd
from tkinter import PhotoImage
from Widget.Frame import *
from Widget.Status import ActiveStatus as c
from Widget.Menu import MainMenu
from Widget.Sound import Sound
from Widget.Result import Result
from Widget.gtts_sound import WordSound
from View.Controller import Control


class Application(tk.Tk):

    # def select_unit_button_command(self):

        # path = '../mimikara_oboeru_n3_vocab_quiz/Data/Dictionary/data{}.csv'.\
        #     format(self.first_frame.unit_select_spin_box.get())
        # try:
        #     self.x = pd.read_csv(path)
        #     self.choice_list = [i for i in range(len(self.x))]
        #     self.index = self.random_choice()
        #     self.word['text'] = self.x.loc[self.index][0]
        #     self.choice_list = [i for i in range(len(self.x))]
        #     self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))
        # except FileNotFoundError:
        #     print('file not found error')
        #     pass

    # def validate(self, action):
    #     # if action == '0':  # currently has a bug for font
    #     #     self.input_frame.kanji_input.delete(0, tk.END)
    #     self.status['text'] = ''
    #     self.meaning['text'] = ''
    #     self.spelling['text'] = ''
    #     self.kanji['text'] = ''
    #     return True

    # def print_result(self, status):
    #
    #     if status:
    #
    #         self.input_frame.kanji_input.delete(0, 'end')
    #         self.input_frame.spelling_input.delete(0, 'end')
    #         self.meaning['text'] = 'meaning: ' + self.x.loc[self.index][1]
    #         self.spelling['text'] = 'spelling: ' + self.x.loc[self.index][2]
    #         self.kanji['text'] = 'kanji: ' + self.x.loc[self.index][3]
    #         self.status.config(foreground='green', text='Correct')
    #         if self.menu_bar.sound.get():
    #             Sound.play_right_sound()
    #         self.choice_list.remove(self.index)
    #         if len(self.choice_list) == 0:
    #             self.display_result()
    #         else:
    #             self.index = self.random_choice()
    #             self.word['text'] = self.x.loc[self.index][0]
    #     else:
    #         if self.index not in self.wrong_ans:
    #             self.wrong_ans.append(self.index)
    #         self.status.config(foreground='red', text='Incorrect')
    #         self.meaning['text'] = 'meaning: ' + self.x.loc[self.index][1]
    #         self.spelling['text'] = 'spelling: ' + self.x.loc[self.index][2]
    #         self.kanji['text'] = 'kanji: ' + self.x.loc[self.index][3]
    #         if self.menu_bar.sound.get():
    #             Sound.play_wrong_sound()
    #     self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))

    # def handle(self, event=None):
    #     try:
    #         if len(self.input_frame.kanji_input.get()) > 0 and len(self.input_frame.spelling_input.get()) > 0:
    #             if self.input_frame.kanji_input.get() == self.x.loc[self.index][3] and \
    #                     self.input_frame.spelling_input.get() == self.x.loc[self.index][2]:
    #                 self.print_result(True)
    #             else:
    #                 self.print_result(False)
    #         elif len(self.input_frame.kanji_input.get()) > 0 and len(self.input_frame.spelling_input.get()) == 0:
    #             if self.input_frame.kanji_input.get() == self.x.loc[self.index][3]:
    #                 self.print_result(True)
    #             else:
    #                 self.print_result(False)
    #         elif len(self.input_frame.kanji_input.get()) == 0 and len(self.input_frame.spelling_input.get()) > 0:
    #             if self.input_frame.spelling_input.get() == self.x.loc[self.index][2]:
    #                 self.print_result(True)
    #             else:
    #                 self.print_result(False)
    #
    #     except ValueError:
    #         pass
    #
    # def random_choice(self):
    #     return random.choice(self.choice_list)
    #
    # def display_result(self):
    #     self.status['text'] = 'Congratulation!!!'
    #     c.add_active_day()
    #     result = Result(self)
    #     result.number_of_wrong_answer.set(result.number_of_wrong_answer.get() + '{}/{}'.format(len(self.wrong_ans),len(self.x)))
    #     # displaying index
    #     unit = int(self.first_frame.unit_select_spin_box.get())
    #     k = 0
    #     if unit == 1:
    #         k = 1
    #     elif unit == 2:
    #         k = 72
    #     elif unit == 3:
    #         k = 121
    #     elif unit == 4:
    #         k = 171
    #     elif unit == 5:
    #         k = 221
    #
    #     self.wrong_ans.sort()
    #     for i in self.wrong_ans:
    #         wrong_result = ', '.join([str(i+k), self.x.iloc[i][0], self.x.iloc[i][1], self.x.iloc[i][2], self.x.iloc[i][3]])
    #         result.wrong_word.insert(tk.END, wrong_result+'\n'+'------------------------'+'\n')
    #
    # def play_sound(self):
    #     WordSound.play_word_sound(self.word['text'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # # the menu bar
        # self.menu_bar = MainMenu(self)
        # self.config(menu=self.menu_bar)

        # setting the select unit part

        self.frame = FirstFrame(self)
        Control.frame_one(self.frame)
        self.frame.pack()



        # logo = PhotoImage(file="../Assets/Image/app_icon.png")
        # self.iconphoto(True, logo)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # self.wrong_ans = []



        # self.first_frame.select_unit_button.config(command=self.select_unit_button_command)
        #
        # self.word = ttk.Label(self, text='', font=('TkDefaultFont', 100))
        # self.word.pack()
        #
        # self.word_count = ttk.Label(self, text='', font=('TkDefaultFont', 30))
        # self.word_count.pack()
        #
        # # frame of label and input
        # self.input_frame = LabelInputFrame(self)
        # self.input_frame.pack(pady=10)
        #
        # # play sound
        # global sound_image
        # sound_image = tk.PhotoImage(file="../Assets/Image/50px_sound_button.gif")
        # sound_btn = tk.Button(self, image=sound_image, command=self.play_sound)
        # sound_btn.pack()
        #
        # # for displaying the status
        # self.status = ttk.Label(self, text='', font=('TkDefaultFont', 100))
        # self.status.pack()
        #
        # # for displaying the results
        # self.meaning = ttk.Label(self, text='', font=('TkDefaultFont', 50))
        # self.meaning.pack()
        # self.spelling = ttk.Label(self, text='', font=('TkDefaultFont', 50))
        # self.spelling.pack()
        # self.kanji = ttk.Label(self, text='', font=('TkDefaultFont', 50))
        # self.kanji.pack()

if __name__ == '__main__':
    app = Application();
    app.mainloop()

