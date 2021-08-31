import tkinter as tk

from functools import partial
from Setting import Load
from View.Widget.Frame import QuizFrame


class FirstFrame(tk.Frame):

    def __init__(self, parent, **kwargs):

        super().__init__(parent, **kwargs)

        self.parent = parent
        self.parent.geometry("600x300+450+200")

        data = Load.get_unit_complete()

        k = 1
        self.dict = []
        for i in range(4):
            for j in range(3):
                label = "Unit {}".format(k)

                buttonborder = tk.Frame(self, highlightbackground="#37d3ff", highlightcolor="#37d3ff",
                                        highlightthickness=2, bd=0)
                buttonborder.grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
                button = tk.Button(buttonborder, text=label + ": {}%".format(data[label]),
                                   width=12,
                                   command=partial(self._change_scene, label))
                self.dict.append([label, button])

                if data[label] == 1:
                    button.config(highlightbackground='green', highlightcolor = 'green', fg = 'green')
                elif data[label] == 0:
                    button.config(highlightbackground='black', highlightcolor = 'black', fg = 'black')
                elif data[label] > 50:
                    button.config(highlightbackground='yellow', highlightcolor = 'yellow', fg='yellow')
                else:
                    button.config(highlightbackground='red', highlightcolor = 'red', fg='red')
                k += 1

    def _change_scene(self, unit):
        self.parent.frame.destroy()
        new_frame = QuizFrame.QuizFrame(self.parent, unit)
        self.parent.frame = new_frame
        self.parent.frame.pack()
