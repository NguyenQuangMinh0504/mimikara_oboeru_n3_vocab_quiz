import tkinter as tk

from Setting import Load
from View import Controller


class FirstFrame(tk.Frame):

    def __init__(self, parent, **kwargs):

        super().__init__(parent, **kwargs)

        self.parent = parent
        self.parent.geometry("400x300+600+200")

        data = Load.load_unit_complete()

        k = 1
        self.dict = []
        for i in range(4):
            for j in range(3):
                label = "Unit {}".format(k)
                button = tk.Button(self, text=label)
                self.dict.append([label, button])
                button.grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
                if data[label]:
                    button.config(highlightbackground='green')
                else:
                    button.config(highlightbackground='red')
                k += 1
        Controller.frame_one(self)