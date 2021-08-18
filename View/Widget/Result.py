import tkinter as tk


class Result(tk.Toplevel):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.number_of_wrong_answer = tk.StringVar(value='Wrong Answers: ')
        tk.Label(self, textvariable=self.number_of_wrong_answer, font=('TkDefaultFont', 20)).pack()
        frame = tk.Frame(self)
        frame.pack()
        self.wrong_word = tk.Text(frame, bd=20, width=50, height=20, font=('TkDefaultFont', 20))
        sb = tk.Scrollbar(frame)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.wrong_word.pack()
        self.wrong_word.config(yscrollcommand=sb.set)
