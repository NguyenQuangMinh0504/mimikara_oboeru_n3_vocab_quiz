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

    def _handle(self, event=None):
        try:
            if self.kanji_input.get() == self.x.loc[self.index][3]:
                self.status['text'] = 'Correct'
                self.meaning['text'] = 'meaning: ' + self.x.loc[self.index][1]
                self.spelling['text'] = 'spelling: ' + self.x.loc[self.index][2]
                self.kanji['text'] = 'kanji: ' + self.x.loc[self.index][3]
                self.choice_list.remove(self.index)
                if len(self.choice_list) == 0:
                    self.status['text'] = 'Congratulation!!!'
                    self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))
                else:
                    self.index = self._random_choice()
                    self.word_input['text'] = self.x.loc[self.index][0]
                    self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))
            else:
                self.status['text'] = 'Incorrect'
                self.meaning['text'] = 'meaning: ' + self.x.loc[self.index][1]
                self.spelling['text'] = 'spelling: ' + self.x.loc[self.index][2]
                self.kanji['text'] = 'kanji: ' + self.x.loc[self.index][3]
                self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))
        except ValueError:
            pass

    def _random_choice(self):
        return random.choice(self.choice_list)

    def __init__(self, *args, **kwargs):
        self.x = pd.read_csv('Dataset/test.csv')
        self.choice_list = [i for i in range(len(self.x))]

        super().__init__(*args, **kwargs)
        self.geometry('1000x600+200+200')
        label = ttk.Label(self, text='QUIZ TIME !!!', font=('TkDefaultFont', 30))
        label.pack()
        word = tk.LabelFrame(self)
        word.pack(fill=tk.Y, pady=10)
        self.index = self._random_choice()

        self.word_input = ttk.Label(word, text=self.x.loc[self.index][0], font=('TkDefaultFont', 100))
        self.word_input.grid(row=0, sticky=tk.W+tk.E, padx=20, columnspan=2)

        self.word_count = ttk.Label(self, text='Word remaining: ' + str(len(self.x)), font=('TkDefaultFont', 30))
        self.word_count.pack()

        # group of input
        container = tk.Frame(self)
        container.pack(pady=10)
        kanji_text = ttk.Label(container, text='Kanji')
        kanji_text.grid(row=1, column=0)
        self.kanji_input = ttk.Entry(container)
        self.kanji_input.grid(row=1, column=1)
        self.kanji_input.config(validate='all',
                                validatecommand=(self.register(self._validate), '%d'))
        self.kanji_input.bind('<Return>', self._handle)
        self.button = tk.Button(container, text='Check', command=self._handle)
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
