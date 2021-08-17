import tkinter as tk

from functools import partial
from Setting import Load
from View.Widget.Frame import QuizFrame


class FirstFrame(tk.Frame):

    def __init__(self, parent, **kwargs):

        super().__init__(parent, **kwargs)

        self.parent = parent
        self.parent.geometry("400x300+600+200")

        data = Load.get_unit_complete()

        k = 1
        self.dict = []
        for i in range(4):
            for j in range(3):
                label = "Unit {}".format(k)
                button = tk.Button(self, text=label, command=partial(self.change_scene, label))
                self.dict.append([label, button])
                button.grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
                if data[label]:
                    button.config(highlightbackground='green')
                else:
                    button.config(highlightbackground='red')
                k += 1

    def change_scene(self, unit):
        self.parent.frame.destroy()
        new_frame = QuizFrame.QuizFrame(self.parent, unit)
        self.parent.frame = new_frame
        self.parent.frame.pack()
