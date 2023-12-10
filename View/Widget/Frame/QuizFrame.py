import tkinter as tk
from tkinter import ttk
from View.Model import Model
from View.Widget.Frame import FirstFrame
from View.Widget.Sound import Sound
from View.Widget.gtts_sound import WordSound
from View.utils import get_example
from Setting import Load
import threading


class QuizFrame(tk.Frame):
    """
    Quiz Frame: Set the application main frame to quiz frame when play quiz
    """

    def __init__(self, parent: tk.Tk, unit):

        super().__init__(parent)
        self.configure(bg='#F6D3CB')
        self.parent = parent

        self.parent.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.unit = unit

        self.model = Model(self)
        self.data = self.model.get_data()

        self.return_btn = ttk.Button(self.parent, text='Return', command=self._change_scene)
        self.return_btn.pack(side='top', anchor='nw')

        self.word = tk.StringVar(value=self.data["word"])
        tk.Label(self, textvariable=self.word, font=('TkDefaultFont', 100), bg='#F6D3CB').pack()
        self.word_count = tk.StringVar(value="Word remaining: " + str(self.data["word_count"]))
        tk.Label(self, textvariable=self.word_count, font=('TkDefaultFont', 30), bg='#F6D3CB').pack()

        self.label_input_frame = self.LabelInputFrame(self)
        self.label_input_frame.pack(pady=10)

        global sound_image
        sound_image = tk.PhotoImage(file=Load.sound_button_path)
        self.sound_btn = tk.Button(self, image=sound_image, bg='#F6D3CB')
        self.sound_btn.pack()
        self.sound_btn.config(command=lambda: WordSound.play_word_sound(word=self.word.get()))

        # for displaying the status
        self.status = tk.Label(self, font=('TkDefaultFont', 50), bg='#F6D3CB')
        self.status.pack()

        # for displaying the results
        self.word_index = tk.StringVar()
        tk.Label(self, textvariable=self.word_index, font=('TkDefaultFont', 40), bg='#F6D3CB').pack()

        self.meaning = tk.StringVar()
        tk.Label(self, textvariable=self.meaning, font=('TkDefaultFont', 40), bg='#F6D3CB').pack()

        self.spelling = tk.StringVar()
        tk.Label(self, textvariable=self.spelling, font=('TkDefaultFont', 40), bg='#F6D3CB').pack()

        self.kanji = tk.StringVar()
        tk.Label(self, textvariable=self.kanji, font=('TkDefaultFont', 40), bg='#F6D3CB').pack()

        self.label_input_frame.spelling_input_btn.bind("<Return>", self.check_answer)
        self.label_input_frame.button.config(command=self.check_answer)

    def update_word(self):
        """Fetching new word. Then update UI"""
        self.data = self.model.get_data()
        self.word.set(self.data["word"])
        self.word_count.set("Word remaining: " + str(self.data["word_count"]))

    def check_answer(self, *args, **kwargs):
        """Check user answer and display result correspondingly."""
        self.word_index.set("word number: " + self.data["word_index"])
        self.meaning.set("meaning: " + self.data["meaning"])
        self.spelling.set("spelling: " + self.data["spelling"])
        self.kanji.set("kanji: " + self.data["kanji"])
        if self.data["spelling"] == self.label_input_frame.spelling_input.get():
            self.status.config(foreground="green", text="Correct")
            self.model.choice_list.remove(self.model.index)
            if len(self.model.choice_list) == 0:
                self.model.display_result()
            else:
                self.model.index = self.model.random_choice()
                self.update_word()
            if self.parent.menu_bar.sound.get():
                Sound.play_right_sound()
            self.update_word()
        else:
            self.status.config(foreground="red", text="Incorrect")
            if self.model.index not in self.model.wrong_ans:
                self.model.wrong_ans.append(self.model.index)
            if self.parent.menu_bar.sound.get():
                Sound.play_wrong_sound()

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

            # Check button
            self.button = ttk.Button(self, text='Check')
            self.button.grid(row=0, column=3, padx=5)

            self.spelling_input_btn.config(validate='all', validatecommand=self.parent.register(self.validate))

            # Example button
            self.example_button = ttk.Button(self, text="Example", command=self.create_new_window)
            self.example_button.grid(row=0, column=4, padx=5)

        def validate(self):
            # if action == '0':  # currently has a bug for font
            #     self.input_frame.kanji_input.delete(0, tk.END)

            self.parent.parent.frame.status['text'] = ''
            self.parent.parent.frame.word_index.set("")
            self.parent.parent.frame.meaning.set("")
            self.parent.parent.frame.spelling.set("")
            self.parent.parent.frame.kanji.set("")
            return True

        def create_new_window(self):
            word = self.parent.word.get()
            new_window = tk.Toplevel(self)
            new_window.title("Word example")
            label = tk.Label(new_window, text="Fetching data from OpenAI API...", font=("Arial", 20))
            label.pack()

            # Using new thread for fetching data from OpenAI API because it take too long.
            def update_data():
                example = get_example(word=word)
                label.config(text=example)

            new_thread = threading.Thread(target=update_data)
            new_thread.start()
