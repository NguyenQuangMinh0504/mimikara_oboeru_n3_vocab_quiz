import random
import pandas as pd
from Widget.Frame import *
from Widget.Status import ActiveStatus as c
from Widget.Menu import MainMenu
from Widget.Sound import Sound


class Application(tk.Tk):

    def select_unit_button_command(self):

        path = '../JapaneseQuizProject/Data/Dictionary/data{}.csv'.\
            format(self.unit_selection_widget.unit_select_spin_box.get())
        try:
            self.x = pd.read_csv(path)
            self.choice_list = [i for i in range(len(self.x))]
            self.index = self.random_choice()
            self.word['text'] = self.x.loc[self.index][0]
            self.choice_list = [i for i in range(len(self.x))]
            self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))
        except FileNotFoundError:
            print('file not found error')
            pass

    def validate(self, action):
        if action == '0':  # currently has a bug for font
            self.input_frame.kanji_input.delete(0, tk.END)
        self.status['text'] = ''
        self.meaning['text'] = ''
        self.spelling['text'] = ''
        self.kanji['text'] = ''
        return True

    def print_result(self, status):

        if status:

            self.input_frame.kanji_input.delete(0, 'end')
            self.input_frame.spelling_input.delete(0, 'end')
            self.meaning['text'] = 'meaning: ' + self.x.loc[self.index][1]
            self.spelling['text'] = 'spelling: ' + self.x.loc[self.index][2]
            self.kanji['text'] = 'kanji: ' + self.x.loc[self.index][3]
            self.status.config(foreground='green', text='Correct')
            if self.menu_bar.sound.get():
                Sound.play_right_sound()
            self.choice_list.remove(self.index)
            if len(self.choice_list) == 0:
                self.status['text'] = 'Congratulation!!!'
                c.add_active_day()
                return None
            else:
                self.index = self.random_choice()
                self.word['text'] = self.x.loc[self.index][0]
        else:

            self.status.config(foreground='red', text='Incorrect')
            self.meaning['text'] = 'meaning: ' + self.x.loc[self.index][1]
            self.spelling['text'] = 'spelling: ' + self.x.loc[self.index][2]
            self.kanji['text'] = 'kanji: ' + self.x.loc[self.index][3]
            if self.menu_bar.sound.get():
                Sound.play_wrong_sould()
        self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))

    def handle(self, event=None):
        try:
            if len(self.input_frame.kanji_input.get()) > 0 and len(self.input_frame.spelling_input.get()) > 0:
                if self.input_frame.kanji_input.get() == self.x.loc[self.index][3] and \
                        self.input_frame.spelling_input.get() == self.x.loc[self.index][2]:
                    self.print_result(True)
                else:
                    self.print_result(False)
            elif len(self.input_frame.kanji_input.get()) > 0 and len(self.input_frame.spelling_input.get()) == 0:
                if self.input_frame.kanji_input.get() == self.x.loc[self.index][3]:
                    self.print_result(True)
                else:
                    self.print_result(False)
            elif len(self.input_frame.kanji_input.get()) == 0 and len(self.input_frame.spelling_input.get()) > 0:
                if self.input_frame.spelling_input.get() == self.x.loc[self.index][2]:
                    self.print_result(True)
                else:
                    self.print_result(False)

        except ValueError:
            pass

    def random_choice(self):
        return random.choice(self.choice_list)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.geometry('1000x600+200+200')

        # the menu bar
        self.menu_bar = MainMenu(self)
        self.config(menu=self.menu_bar)

        # setting the select unit part
        self.unit_selection_widget = UnitSelectionFrame(self)
        self.unit_selection_widget.pack()
        self.unit_selection_widget.select_unit_button.config(command=self.select_unit_button_command)

        self.word = ttk.Label(self, text='', font=('TkDefaultFont', 100))
        self.word.pack()

        self.word_count = ttk.Label(self, text='', font=('TkDefaultFont', 30))
        self.word_count.pack()

        # frame of label and input
        self.input_frame = LabelInputFrame(self)
        self.input_frame.pack(pady=10)

        # for displaying the status
        self.status = ttk.Label(self, text='', font=('TkDefaultFont', 100))
        self.status.pack()

        # for displaying the results
        self.meaning = ttk.Label(self, text='', font=('TkDefaultFont', 50))
        self.meaning.pack()
        self.spelling = ttk.Label(self, text='', font=('TkDefaultFont', 50))
        self.spelling.pack()
        self.kanji = ttk.Label(self, text='', font=('TkDefaultFont', 50))
        self.kanji.pack()
