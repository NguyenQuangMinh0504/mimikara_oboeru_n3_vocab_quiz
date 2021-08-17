import tkinter as tk
from tkinter import ttk

from View import Controller
from View.Model import Model


class QuizFrame(tk.Frame):

    def __init__(self, parent, unit):

        super().__init__(parent)

        self.parent = parent
        self.parent.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

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
        self.sound_btn.pack()

        Controller.play_sound(self)
        self.model.load_data()
        self.model.load()

        # for displaying the status
        self.status = tk.Label(self, font=('TkDefaultFont', 100))
        self.status.pack()

        # for displaying the results
        self.meaning = tk.StringVar()
        tk.Label(self, textvariable=self.meaning, font=('TkDefaultFont', 50)).pack()

        self.spelling = tk.StringVar()
        tk.Label(self, textvariable=self.spelling, font=('TkDefaultFont', 50)).pack()

        self.kanji = tk.StringVar()
        tk.Label(self, textvariable=self.kanji, font=('TkDefaultFont', 50)).pack()

        Controller.button_validate(self)

        self.label_input_frame.spelling_input_btn.bind("<Return>", self.model.handle)
        self.label_input_frame.button.config(command=self.model.handle)

    class LabelInputFrame(tk.Frame):

        def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)

            tk.Label(self, text='Spelling').grid(row=0, column=1, sticky=tk.W, padx=5)

            self.spelling_input = tk.StringVar()
            self.spelling_input_btn = tk.Entry(self, textvariable=self.spelling_input)
            self.spelling_input_btn.grid(row=0, column=2)

            self.button = tk.Button(self, text='Check')
            self.button.grid(row=0, column=3)