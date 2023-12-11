import random
from Setting import Load


class Model:
    def __init__(self, unit: str):
        self.wrong_ans = []
        self.data = Load.load_data(unit.replace(" ", "").lower())
        self.choice_list = [i for i in range(len(self.data))]
        self.index = self.random_choice()

    def get_data(self) -> dict:
        return {"word": self.data.iloc[self.index][1],
                "word_count": len(self.choice_list),
                "spelling": self.data.iloc[self.index][3],
                "word_index": str(self.data.iloc[self.index][0]),
                "meaning": self.data.iloc[self.index][2],
                "kanji": self.data.iloc[self.index][4],
                }

    def random_choice(self):
        return random.choice(self.choice_list)

    def get_right_answer_percentage(self):
        """Return right answer percentage"""
        return int((1 - len(self.wrong_ans)/len(self.data)) * 100)
