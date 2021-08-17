import random
import tkinter as tk
from Setting import Load
from View.Widget.Sound import Sound
from View.Widget.Status import ActiveStatus
from View.Widget.Result import Result


class Model:
    def __init__(self, frame):
        self.frame = frame
        self.wrong_ans = []

    def load(self):
        self.choice_list = [i for i in range(len(self.data))]
        self.index = self.random_choice()
        self.word = self.data.loc[self.index][0]
        self.word_count = len(self.data)
        self.frame.word.set(self.word)
        self.frame.word_count.set("Word remaining " + str(self.word_count))

    def load_data(self):
        self.data = Load.load_data(self.frame.unit.replace(" ", '').lower())

    def random_choice(self):
        return random.choice(self.choice_list)

    def print_result(self, status):

        if status:
            self.choice_list.remove(self.index)
            self.frame.label_input_frame.spelling_input.set('')
            self.frame.meaning.set('meaning: ' + self.data.loc[self.index][1])
            self.frame.spelling.set('spelling: ' + self.data.loc[self.index][2])
            self.frame.kanji.set('kanji: ' + self.data.loc[self.index][3])
            self.frame.status.config(foreground='green', text='Correct')
            if self.frame.parent.menu_bar.sound.get():
                Sound.play_right_sound()

            if len(self.choice_list) == 0:
                self.display_result()
            else:
                self.index = self.random_choice()
                self.frame.word.set(self.data.loc[self.index][0])

        else:
            if self.index not in self.wrong_ans:
                self.wrong_ans.append(self.index)
            self.frame.status.config(foreground='red', text='Incorrect')
            self.frame.meaning.set('meaning: ' + self.data.loc[self.index][1])
            self.frame.spelling.set('spelling: ' + self.data.loc[self.index][2])
            self.frame.kanji.set('kanji: ' + self.data.loc[self.index][3])

            if self.frame.parent.menu_bar.sound.get():
                Sound.play_wrong_sound()
        self.frame.word_count.set('Word remaining: ' + str(len(self.choice_list)))

    def handle(self, event=None):
        if self.frame.label_input_frame.spelling_input.get() == self.data.loc[self.index][2]:
            self.print_result(True)
        else:
            self.print_result(False)

    def display_result(self):
        self.frame.status['text'] = 'Congratulation!!!'
        ActiveStatus.add_active_day()
        result = Result(self.frame.parent)
        result.number_of_wrong_answer.set(result.number_of_wrong_answer.get() +
                                          '{}/{}'.format(len(self.wrong_ans), len(self.data)))
        # displaying index
        unit = int(self.frame.unit.replace("Unit ", ""))
        k = 0
        if unit == 1:
            k = 1
        elif unit == 2:
            k = 72
        elif unit == 3:
            k = 121
        elif unit == 4:
            k = 171
        elif unit == 5:
            k = 221
        self.wrong_ans.sort()
        for i in self.wrong_ans:
            wrong_result = ', '.join([str(i+k), self.data.iloc[i][0], self.data.iloc[i][1],
                                      self.data.iloc[i][2], self.data.iloc[i][3]])
            result.wrong_word.insert('end', wrong_result+'\n'+'------------------------'+'\n')

