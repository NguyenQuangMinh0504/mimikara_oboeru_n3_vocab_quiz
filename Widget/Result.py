import tkinter as tk
from tkinter import ttk


class Result(tk.Toplevel):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        frame = ttk.LabelFrame(self, text='Wrong word:')
        frame.pack()
        self.wrong_word = tk.Text(frame, bd=20, width=50, height=20)
        sb = tk.Scrollbar(frame)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.wrong_word.pack()
        self.wrong_word.config(yscrollcommand=sb.set)





