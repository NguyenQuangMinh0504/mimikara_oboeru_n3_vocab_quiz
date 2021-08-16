
from tkinter import PhotoImage
from Widget.Frame import *
from Widget.Status import ActiveStatus as c
from Widget.Menu import MainMenu
from View import Model
from Widget.Sound import Sound
from Widget.Result import Result


class Application(tk.Tk):

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # the menu bar
        self.menu_bar = MainMenu(self)
        self.config(menu=self.menu_bar)

        # setting the select unit part

        self.frame = FirstFrame(self)
        self.frame.pack()

        # setting the logo
        logo = PhotoImage(file="../Assets/Image/app_icon-2.gif")
        self.iconphoto(True, logo)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # self.wrong_ans = []


if __name__ == '__main__':
    app = Application()
    app.mainloop()

