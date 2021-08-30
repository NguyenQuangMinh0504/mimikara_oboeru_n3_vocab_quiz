import tkinter as tk


class Result(tk.Toplevel):
    """
    Popup Screen showing the result when finish the quiz
    """
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.number_of_wrong_answer = tk.StringVar(value='Wrong Answers: ')
        tk.Label(self, textvariable=self.number_of_wrong_answer, font=('TkDefaultFont', 20)).pack()

        # scrollable frame for display the wrong words
        frame = tk.Frame(self)
        frame.pack()

        # config the scrollbar
        sb = tk.Scrollbar(frame)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

        self.wrong_word = tk.Text(frame, bd=20, width=50, height=20, font=('TkDefaultFont', 20))
        self.wrong_word.pack()
        self.wrong_word.config(yscrollcommand=sb.set)
