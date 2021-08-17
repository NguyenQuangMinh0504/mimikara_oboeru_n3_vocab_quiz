import tkinter as tk
from tkinter import ttk
from Setting import Load
from View import Controller
from View.Model import Model


class FirstFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent

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


class QuizFrame(tk.Frame):

    def __init__(self, parent, unit):
        super().__init__(parent)
        self.parent = parent
        self.unit = unit
        self.model = Model(self)
        self.word = tk.StringVar()
        ttk.Label(self, textvariable=self.word, font=('TkDefaultFont', 100)).pack()
        self.word_count = tk.StringVar()
        ttk.Label(self, textvariable=self.word_count, font=('TkDefaultFont', 30)).pack()
        self.label_input_frame = self.LabelInputFrame(self)
        self.label_input_frame.pack(pady=10)
        global sound_image
        sound_image = tk.PhotoImage(file="../Assets/Image/50px_sound_button.gif")
        self.sound_btn = tk.Button(self, image=sound_image)
        Controller.play_sound(self)
        self.model.load_data()
        self.model.load()
        self.sound_btn.pack()

        # for displaying the status
        self.status = tk.StringVar()
        tk.Label(self, text=self.status, font=('TkDefaultFont', 100)).pack()

        # for displaying the results
        self.meaning = tk.StringVar()
        tk.Label(self, text=self.meaning, font=('TkDefaultFont', 50)).pack()
        self.spelling = tk.StringVar()
        tk.Label(self, text=self.spelling, font=('TkDefaultFont', 50)).pack()
        self.kanji = tk.StringVar()
        tk.Label(self, text=self.kanji, font=('TkDefaultFont', 50)).pack()

        Controller.button_validate(self)

    class LabelInputFrame(tk.Frame):
        def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)

            tk.Label(self, text='Spelling').grid(row=0, column=1, sticky=tk.W, padx=5)
            self.spelling_input = tk.StringVar()
            self.spelling_input_btn = tk.Entry(self, textvariable=self.spelling_input)
            self.spelling_input_btn.grid(row=0, column=2)

            # self.spelling_input.bind('<Return>', parent.handle)

            self.button = tk.Button(self, text='Check')
            # self.button.config(command=parent.handle)
            self.button.grid(row=0, column=3)
