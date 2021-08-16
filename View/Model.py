import random


class Model:
    def __init__(self, application):
        self.application = application
        self.data = None
        self.choice_list = [i for i in range(len(self.data))]
        self.index = self.random_choice()
        self.word = self.data.loc[self.index][0]
        self.word_count = len(self.data)

    def load(self):
        self.application.frame.word.set(self.word)
        self.application.frame.word_count.set(self.word_count)
        print(self.application.frame.unit)

    def random_choice(self):
        return random.choice(self.choice_list)

