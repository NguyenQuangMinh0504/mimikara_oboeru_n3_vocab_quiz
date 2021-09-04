import tkinter as tk
from tkinter import ttk

from View.Model import Model
from View.Widget.Frame import FirstFrame
from Setting import Load


class QuizFrame(tk.Frame):
    """
    Quiz Frame: Set the application main frame to quiz frame when play quiz
    """

    def __init__(self, parent, unit):

        super().__init__(parent)
        self.configure(bg='#F6D3CB')
        self.parent = parent

        self.parent.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.unit = unit

        self.return_btn = ttk.Button(self.parent, text='Return', command=self._change_scene)
        self.return_btn.pack(side='top', anchor='nw')

        self.model = Model(self)

        self.word = tk.StringVar()
        tk.Label(self, textvariable=self.word, font=('TkDefaultFont', 100), bg='#F6D3CB').pack()

        self.word_count = tk.StringVar()
        tk.Label(self, textvariable=self.word_count, font=('TkDefaultFont', 30), bg='#F6D3CB').pack()

        self.label_input_frame = self.LabelInputFrame(self)
        self.label_input_frame.pack(pady=10)

        global sound_image
        sound_image = tk.PhotoImage(file=Load.sound_button_path)
        self.sound_btn = tk.Button(self, image=sound_image, bg='#F6D3CB')
        self.sound_btn.pack()

        self.model.play_sound()
        self.model.load_data()
        self.model.load()

        # for displaying the status
        self.status = tk.Label(self, font=('TkDefaultFont', 50), bg='#F6D3CB')
        self.status.pack()

        # for displaying the results
        self.meaning = tk.StringVar()
        tk.Label(self, textvariable=self.meaning, font=('TkDefaultFont', 50), bg='#F6D3CB').pack()

        self.spelling = tk.StringVar()
        tk.Label(self, textvariable=self.spelling, font=('TkDefaultFont', 50), bg='#F6D3CB').pack()

        self.kanji = tk.StringVar()
        tk.Label(self, textvariable=self.kanji, font=('TkDefaultFont', 50), bg='#F6D3CB').pack()
        self.label_input_frame.spelling_input_btn.bind("<Return>", self.model.handle)
        self.label_input_frame.button.config(command=self.model.handle)

    def _change_scene(self):
        self.parent.frame.destroy()
        self.return_btn.destroy()
        new_frame = FirstFrame.FirstFrame(self.parent)
        self.parent.frame = new_frame
        self.parent.frame.pack()

    class LabelInputFrame(tk.Frame):

        def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)
            self.configure(bg='#F6D3CB')
            self.parent = parent

            tk.Label(self, text='Spelling', bg='#F6D3CB').grid(row=0, column=1, sticky=tk.W, padx=5)

            self.spelling_input = tk.StringVar()
            self.spelling_input_btn = tk.Entry(self, textvariable=self.spelling_input)
            self.spelling_input_btn.grid(row=0, column=2)

            self.button = ttk.Button(self, text='Check')
            self.button.grid(row=0, column=3, padx=5)
            self.spelling_input_btn.config(validate='all', validatecommand=self.parent.register(self.validate))

        def validate(self):
            # if action == '0':  # currently has a bug for font
            #     self.input_frame.kanji_input.delete(0, tk.END)

            self.parent.parent.frame.status['text'] = ''
            self.parent.parent.frame.meaning.set("")
            self.parent.parent.frame.spelling.set("")
            self.parent.parent.frame.kanji.set("")
            return True
