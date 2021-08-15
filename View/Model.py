import random


class Model:
    def __init__(self):
        self.data = None
        self.choice_list = [i for i in range(len(self.data))]



# def select_unit_button_command(self):

        choice_list = [i for i in range(len(self.x))]
        self.index = self.random_choice()
        self.word['text'] = self.x.loc[self.index][0]

        self.word_count['text'] = 'Word remaining: ' + str(len(self.choice_list))

    def random_choice(self):
        return random.choice(self.choice_list)