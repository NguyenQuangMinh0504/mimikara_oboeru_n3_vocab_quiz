import random
from View.Widget.Sound import Sound
from View.Widget.Status import ActiveStatus
from View.Widget.Result import Result
from Setting import Load


class Model:
    def __init__(self, frame):
        self.frame = frame
        self.wrong_ans = []
        self.data = Load.load_data(self.frame.unit.replace(" ", "").lower())
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
