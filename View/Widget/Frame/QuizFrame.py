import tkinter as tk
from tkinter import ttk
from View.Model import Model
from View.Widget.Frame import FirstFrame
from View.Widget.Sound import Sound
from View.Widget.Result import Result
from View.Widget.gtts_sound import WordSound
from View.Widget.Status import ActiveStatus
from View.utils import get_example
from Setting import Load
import threading


class QuizFrame(tk.Frame):
    """
    Quiz Frame: Set the application main frame to quiz frame when play quiz
    """

    def __init__(self, parent: tk.Tk, unit):

        super().__init__(parent)
        self.parent = parent
        self.unit = unit

        def center_window():
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screendepth()
            window_width = 600
            window_height = 700
            # Calculate center coordinates
            center_x = int((screen_width - window_width) / 2)
            center_y = int((screen_height - window_height) / 2)
            # Set window position
            self.parent.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        center_window()

        self.model = Model(unit)
        self.data = self.model.get_data()

        self.return_btn = ttk.Button(self.parent, text='Return', command=self._change_scene)
        self.return_btn.pack(side='top', anchor='nw')

        self.word = tk.StringVar(value=self.data["word"])
        tk.Label(self, textvariable=self.word, font=('TkDefaultFont', 100)).pack()
        self.word_count = tk.StringVar(value="Word remaining: " + str(self.data["word_count"]))
        tk.Label(self, textvariable=self.word_count, font=('TkDefaultFont', 30)).pack()

        # self.label_input_frame = self.LabelInputFrame(self)
        # self.label_input_frame.pack(pady=10)

        frame = tk.Frame(self)
        frame.pack(pady=10)
        tk.Label(frame, text="Spelling").pack(side="left")
        self.spelling_input = tk.StringVar()
        self.spelling_input_btn = tk.Entry(frame, textvariable=self.spelling_input)
        self.spelling_input_btn.pack(side="left", padx=10)

        # Check button
        self.button = ttk.Button(frame, text='Check')
        self.button.pack(side="left", padx=10)

        self.spelling_input_btn.config(validate='all', validatecommand=self.parent.register(self.validate))

        # Example button
        self.example_button = ttk.Button(frame, text="Example", command=self.create_new_window)
        self.example_button.pack(side="left", padx=10)

        global sound_image
        sound_image = tk.PhotoImage(file=Load.sound_button_path)
        self.sound_btn = tk.Button(self, image=sound_image)
        self.sound_btn.pack(side="top")
        self.sound_btn.config(command=lambda: WordSound.play_word_sound(word=self.word.get()))

        # for displaying the status
        self.status = tk.Label(self, font=('TkDefaultFont', 50))
        self.status.pack()

        # for displaying the results
        self.word_index = tk.StringVar()
        tk.Label(self, textvariable=self.word_index, font=('TkDefaultFont', 40)).pack()

        self.meaning = tk.StringVar()
        tk.Label(self, textvariable=self.meaning, font=('TkDefaultFont', 40)).pack()

        self.spelling = tk.StringVar()
        tk.Label(self, textvariable=self.spelling, font=('TkDefaultFont', 40)).pack()

        self.kanji = tk.StringVar()
        tk.Label(self, textvariable=self.kanji, font=('TkDefaultFont', 40)).pack()

        self.spelling_input_btn.bind("<Return>", self.check_answer)
        self.button.config(command=self.check_answer)

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
        if self.data["spelling"] == self.spelling_input.get():
            self.status.config(foreground="green", text="Correct")
            self.model.choice_list.remove(self.model.index)
            if len(self.model.choice_list) == 0:
                self.display_final_result()
            else:
                self.model.index = self.model.random_choice()
                self.update_word()
            if self.parent.menu_bar.sound.get():
                Sound.play_right_sound()
        else:
            self.status.config(foreground="red", text="Incorrect")
            if self.model.index not in self.model.wrong_ans:
                self.model.wrong_ans.append(self.model.index)
            if self.parent.menu_bar.sound.get():
                Sound.play_wrong_sound()

    def display_final_result(self):
        self.status.config(text="Congratulation!!!", foreground="green")

        # Add active day
        ActiveStatus.add_active_day()

        # Update right answer percentage
        data = Load.get_unit_complete()
        data[self.unit] = max(self.model.get_right_answer_percentage(), data[self.unit])
        Load.set_unit_complete(data)

        result = Result(self.parent)
        result.number_of_wrong_answer.set(result.number_of_wrong_answer.get() +
                                          '{}/{}'.format(len(self.model.wrong_ans), len(self.model.data)))

        self.model.wrong_ans.sort()
        for i in self.model.wrong_ans:
            wrong_result = ', '.join([str(self.model.data.iloc[i][0]),
                                      self.model.data.iloc[i][1],
                                      self.model.data.iloc[i][2],
                                      self.model.data.iloc[i][3],
                                      self.model.data.iloc[i][4]])
            result.wrong_word.insert('end', wrong_result+'\n'+'------------------------'+'\n')

    def _change_scene(self):
        self.parent.frame.destroy()
        self.return_btn.destroy()
        new_frame = FirstFrame.FirstFrame(self.parent)
        self.parent.frame = new_frame
        self.parent.frame.pack()

    def validate(self):
        self.status['text'] = ''
        self.word_index.set("")
        self.meaning.set("")
        self.spelling.set("")
        self.kanji.set("")
        return True

    def create_new_window(self):
        word = self.word.get()
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
