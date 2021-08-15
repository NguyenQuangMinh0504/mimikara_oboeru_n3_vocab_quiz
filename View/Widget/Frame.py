import tkinter as tk
from tkinter import ttk
from Setting import Load
from View import Controller


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


class QuizFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.word = ttk.Label(self, text='Something', font=('TkDefaultFont', 100))
        self.word.pack()
        self.word_count = ttk.Label(self, text='Something', font=('TkDefaultFont', 30))
        self.word_count.pack()
        label_input_frame = self.LabelInputFrame(self)
        label_input_frame.pack(pady=10)
        global sound_image
        sound_image = tk.PhotoImage(file="../Assets/Image/50px_sound_button.gif")
        self.sound_btn = tk.Button(self, image=sound_image)
        Controller.play_sound(self)
        self.sound_btn.pack()

        # for displaying the status
        self.status = ttk.Label(self, text='Something', font=('TkDefaultFont', 100))
        self.status.pack()

        # for displaying the results
        self.meaning = ttk.Label(self, text='Something', font=('TkDefaultFont', 50))
        self.meaning.pack()
        self.spelling = ttk.Label(self, text='Something', font=('TkDefaultFont', 50))
        self.spelling.pack()
        self.kanji = ttk.Label(self, text='Something', font=('TkDefaultFont', 50))
        self.kanji.pack()

    class LabelInputFrame(tk.Frame):
        def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)
            ttk.Label(self, text='Kanji').grid(row=0, column=0, sticky=tk.W, padx=5)
            self.kanji_input = ttk.Entry(self)
            self.kanji_input.grid(row=1, column=0)

            # self.kanji_input.config(validate='all',
            #                         validatecommand=(parent.register(parent.validate), '%d'))
            # self.kanji_input.bind('<Return>', parent.handle)

            ttk.Label(self, text='Spelling').grid(row=0, column=1, sticky=tk.W, padx=5)
            self.spelling_input = ttk.Entry(self)
            self.spelling_input.grid(row=1, column=1)
            # self.spelling_input.config(validate='all',
            #                            validatecommand=(parent.register(parent.validate), '%d'))
            # self.spelling_input.bind('<Return>', parent.handle)

            # self.button = tk.Button(self, text='Check', command=parent.handle)
            # self.button.grid(row=1, column=2)
