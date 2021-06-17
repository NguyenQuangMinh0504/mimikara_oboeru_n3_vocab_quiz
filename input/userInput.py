import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        word_label = ttk.Label(self, text='Word')
        word_label.grid(row=0, column=0)
        word_input = ttk.Entry(self)
        word_input.grid(row=1, column=0)
        spelling_label = ttk.Label(self, text='Spelling')
        spelling_label.grid(row=0, column=1)
        spelling_input = ttk.Entry(self)
        spelling_input.grid(row=1, column=1)
        meaning_label = ttk.Label(self, text='Meaning')
        meaning_label.grid(row=2, column=0)
        meaning_input1 = ttk.Entry(self)
        meaning_input1.grid(row=3, column=0)
        meaning_input2 = ttk.Entry(self)
        meaning_input2.grid(row=4, column=0)
        meaning_input3 = ttk.Entry(self)
        meaning_input3.grid(row=5, column=0)
        kanji_label = ttk.Label(self, text='Kanji')
        kanji_label.grid(row=2, column=1)
        kanji_input1 = ttk.Entry(self)
        kanji_input1.grid(row=3, column=1)
        kanji_input2 = ttk.Entry(self)
        kanji_input2.grid(row=4, column=1)
        kanji_input3 = ttk.Entry(self)
        kanji_input3.grid(row=5, column=1)



if __name__ == '__main__':
    app = Application()
    app.mainloop()
