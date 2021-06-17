import pandas as pd
import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        x = pd.read_csv('Dataset/data1.csv')
        super().__init__(*args, **kwargs)
        ttk.Label(self, text='QUIZ TIME !!!', font=('TkDefaultFont', 30)).grid(row=0, sticky=tk.W+tk.E, padx=20)
        self.geometry('+450+300')
        word = tk.LabelFrame(self,height=200, width=200)
        word.grid(row=1, padx=20, pady=20)
        word_input = tk.Label(word, text=x.loc[0][0], font=('TkDefaultFont', 150))
        word_input.grid(row=0, sticky=tk.W+tk.E, padx=20)


if __name__ == '__main__':
    app = Application()
    app.mainloop()




