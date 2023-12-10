import random
from Setting import Load


class Model:
    def __init__(self, unit: str):
        self.wrong_ans = []
        self.data = Load.load_data(unit.replace(" ", "").lower())
        self.load()

    def load(self):
        """Loading data"""
        self.choice_list = [i for i in range(len(self.data))]
        self.index = self.random_choice()
        self.word = self.data.loc[self.index][1]
        self.word_count = len(self.data)

    def get_data(self) -> dict:
        return {"word": self.data.loc[self.index][1],
                "word_count": len(self.choice_list),
                "spelling": self.data.loc[self.index][3],
                "word_index": str(self.data.loc[self.index][0]),
                "meaning": self.data.loc[self.index][2],
                "kanji": self.data.loc[self.index][4],
                }

    def random_choice(self):
        return random.choice(self.choice_list)

    def get_right_answer_percentage(self):
        """Return right answer percentage"""
        return int((1 - len(self.wrong_ans)/len(self.data)) * 100)
