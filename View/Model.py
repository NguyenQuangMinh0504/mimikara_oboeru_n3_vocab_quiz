import random
from View.Widget.Sound import Sound
from View.Widget.Status import ActiveStatus
from View.Widget.Result import Result
from View.Widget.gtts_sound import WordSound
from Setting import Load


class Model:
    def __init__(self, frame):
        self.frame = frame
        self.wrong_ans = []
        self.data = Load.load_data(self.frame.unit.replace(" ", "").lower())
        self.load()

    def load(self):
        self.choice_list = [i for i in range(len(self.data))]
        self.index = self.random_choice()
        self.word = self.data.loc[self.index][1]
        self.word_count = len(self.data)
        self.frame.word.set(self.word)
        self.frame.word_count.set("Word remaining: " + str(self.word_count))

    def random_choice(self):
        return random.choice(self.choice_list)

    def print_result(self, status):

        if status:
            self.choice_list.remove(self.index)
            self.frame.label_input_frame.spelling_input.set('')
            self.frame.word_index.set('word number: ' + str(self.data.loc[self.index][0]))
            self.frame.meaning.set('meaning: ' + self.data.loc[self.index][2])
            self.frame.spelling.set('spelling: ' + self.data.loc[self.index][3])
            self.frame.kanji.set('kanji: ' + self.data.loc[self.index][4])
            self.frame.status.config(foreground='green', text='Correct')
            if self.frame.parent.menu_bar.sound.get():
                Sound.play_right_sound()

            if len(self.choice_list) == 0:
                self.display_result()
            else:
                self.index = self.random_choice()
                self.frame.word.set(self.data.loc[self.index][1])

        else:
            if self.index not in self.wrong_ans:
                self.wrong_ans.append(self.index)
            self.frame.status.config(foreground='red', text='Incorrect')
            self.frame.word_index.set('word number: ' + str(self.data.loc[self.index][0]))
            self.frame.meaning.set('meaning: ' + self.data.loc[self.index][2])
            self.frame.spelling.set('spelling: ' + self.data.loc[self.index][3])
            self.frame.kanji.set('kanji: ' + self.data.loc[self.index][4])

            if self.frame.parent.menu_bar.sound.get():
                Sound.play_wrong_sound()
        self.frame.word_count.set('Word remaining: ' + str(len(self.choice_list)))

    def handle(self, event=None):
        if self.frame.label_input_frame.spelling_input.get() == self.data.loc[self.index][3]:
            self.print_result(True)
        else:
            self.print_result(False)

    def display_result(self):
        self.frame.status['text'] = 'Congratulation!!!'
        ActiveStatus.add_active_day()
        data = Load.get_unit_complete()
        data[self.frame.unit] = max(int((1-len(self.wrong_ans)/len(self.data))*100), data[self.frame.unit])
        Load.set_unit_complete(data)

        result = Result(self.frame.parent)
        result.number_of_wrong_answer.set(result.number_of_wrong_answer.get() +
                                          '{}/{}'.format(len(self.wrong_ans), len(self.data)))

        self.wrong_ans.sort()
        for i in self.wrong_ans:
            wrong_result = ', '.join([str(self.data.iloc[i][0]), self.data.iloc[i][1], self.data.iloc[i][2],
                                      self.data.iloc[i][3], self.data.iloc[i][4]])
            result.wrong_word.insert('end', wrong_result+'\n'+'------------------------'+'\n')

    def play_sound(self):
        self.frame.sound_btn.config(command=lambda: WordSound.play_word_sound(self.frame.word.get()))
