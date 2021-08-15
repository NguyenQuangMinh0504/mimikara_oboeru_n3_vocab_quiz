class Control:
    @staticmethod
    def frame_one(frame):
        for i in frame.dict.values:
            i.config(command=lambda :print('hello kitty'))



