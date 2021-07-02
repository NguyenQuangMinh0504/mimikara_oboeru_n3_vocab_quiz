import random
import pandas as pd
import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def _validate(self, action):
        # if action == '0': # currently has a bug for font
        #     self.kanji_input.delete(0, tk.END)
        self.status['text'] = ''
        self.meaning['text'] = ''
        self.spelling['text'] = ''
        self.kanji['text'] = ''
        return True

    def _print_result(self, status):
        if status:
            self.status['text'] = 'Correct'
            self.choice_list.remove(self.index)
            if len(self.choice_list) == 0:
                self.status['text'] = 'Congratulation!!!'
            else:
                self.index = self._random_choice()
                self.word['text'] = self.x.loc[self.index][0]
        else:
            self.status['text'] = 'Incorrect'
        self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))
        self.meaning['text'] = 'meaning: ' + self.x.loc[self.index][1]
        self.spelling['text'] = 'spelling: ' + self.x.loc[self.index][2]
        self.kanji['text'] = 'kanji: ' + self.x.loc[self.index][3]

    def _handle(self, event=None):
        try:
            if len(self.kanji_input.get()) > 0 and len(self.spelling_input.get()) > 0:
                if self.kanji_input.get() == self.x.loc[self.index][3]:
                    self._print_result(True)
                else:
                    self._print_result(False)
            elif len(self.kanji_input.get()) > 0 and len(self.spelling_input.get()) == 0:
                if self.kanji_input.get() == self.x.loc[self.index][3]:
                    self._print_result(True)
                else:
                    self._print_result(False)
            elif len(self.kanji_input.get()) == 0 and len(self.spelling_input.get()) > 0:
                if self.spelling_input.get() == self.x.loc[self.index][2]:
                    self._print_result(True)
                else:
                    self._print_result(False)

        except ValueError:
            pass

    def _random_choice(self):
        return random.choice(self.choice_list)

    def __init__(self, *args, **kwargs):
        self.x = pd.read_csv('Dataset/data2.csv')
        self.choice_list = [i for i in range(len(self.x))]

        super().__init__(*args, **kwargs)
        self.geometry('1000x600+200+200')
        self.index = self._random_choice()

        self.word = ttk.Label(self, text=self.x.loc[self.index][0], font=('TkDefaultFont', 100))
        self.word.pack()

        self.word_count = ttk.Label(self, text='Word remaining: ' + str(len(self.x)), font=('TkDefaultFont', 30))
        self.word_count.pack()

        # group of input
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)
        ttk.Label(input_frame, text='Kanji').grid(row=0, column=0, sticky=tk.W, padx=5)
        self.kanji_input = ttk.Entry(input_frame)
        self.kanji_input.grid(row=1, column=0)
        self.kanji_input.config(validate='all',
                                validatecommand=(self.register(self._validate), '%d'))
        self.kanji_input.bind('<Return>', self._handle)

        ttk.Label(input_frame, text='Spelling').grid(row=0, column=1, sticky=tk.W, padx=5)
        self.spelling_input = ttk.Entry(input_frame)
        self.spelling_input.grid(row=1, column=1)
        self.spelling_input.bind('<Return>', self._handle)

        self.button = tk.Button(input_frame, text='Check', command=self._handle)
        self.button.grid(row=1, column=2)

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


if __name__ == '__main__':
    app = Application()
    app.mainloop()
