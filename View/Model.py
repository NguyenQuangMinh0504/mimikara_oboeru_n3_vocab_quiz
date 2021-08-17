import random
from Setting import Load

class Model:
    def __init__(self, frame):
        self.frame = frame

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
            self.frame.meaning.set('meaning: ' + self.x.loc[self.index][1])
            self.frame.spelling.set('spelling: ' + self.x.loc[self.index][2])
            self.frame.kanji.set('kanji: ' + self.x.loc[self.index][3])
            self.frame.status.config(foreground='green', text='Correct')
            if self.menu_bar.sound.get():
                Sound.play_right_sound()


            if len(self.choice_list) == 0:
                self.display_result()
            else:
                self.index = self.random_choice()
                self.word['text'] = self.x.loc[self.index][0]
        else:
            if self.index not in self.wrong_ans:
                self.wrong_ans.append(self.index)
            self.status.config(foreground='red', text='Incorrect')
            self.meaning['text'] = 'meaning: ' + self.x.loc[self.index][1]
            self.spelling['text'] = 'spelling: ' + self.x.loc[self.index][2]
            self.kanji['text'] = 'kanji: ' + self.x.loc[self.index][3]
            if self.menu_bar.sound.get():
                Sound.play_wrong_sound()
        self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))

    def handle(self, event=None):
        try:
            if len(self.input_frame.kanji_input.get()) > 0 and len(self.input_frame.spelling_input.get()) > 0:
                if self.input_frame.kanji_input.get() == self.x.loc[self.index][3] and \
                        self.input_frame.spelling_input.get() == self.x.loc[self.index][2]:
                    self.print_result(True)
                else:
                    self.print_result(False)
            elif len(self.input_frame.kanji_input.get()) > 0 and len(self.input_frame.spelling_input.get()) == 0:
                if self.input_frame.kanji_input.get() == self.x.loc[self.index][3]:
                    self.print_result(True)
                else:
                    self.print_result(False)
            elif len(self.input_frame.kanji_input.get()) == 0 and len(self.input_frame.spelling_input.get()) > 0:
                if self.input_frame.spelling_input.get() == self.x.loc[self.index][2]:
                    self.print_result(True)
                else:
                    self.print_result(False)

        except ValueError:
            pass

    # def display_result(self):
    #     self.status['text'] = 'Congratulation!!!'
    #     c.add_active_day()
    #     result = Result(self)
    #     result.number_of_wrong_answer.set(result.number_of_wrong_answer.get() + '{}/{}'.format(len(self.wrong_ans),len(self.x)))
    #     # displaying index
    #     unit = int(self.first_frame.unit_select_spin_box.get())
    #     k = 0
    #     if unit == 1:
    #         k = 1
    #     elif unit == 2:
    #         k = 72
    #     elif unit == 3:
    #         k = 121
    #     elif unit == 4:
    #         k = 171
    #     elif unit == 5:
    #         k = 221
    #
    #     self.wrong_ans.sort()
    #     for i in self.wrong_ans:
    #         wrong_result = ', '.join([str(i+k), self.x.iloc[i][0], self.x.iloc[i][1], self.x.iloc[i][2], self.x.iloc[i][3]])
    #         result.wrong_word.insert(tk.END, wrong_result+'\n'+'------------------------'+'\n')

