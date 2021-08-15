import tkinter as tk
from testing.testing2.something import Something

class app(tk.Tk):

    def __init__(self):
        super().__init__()
        self.something = Something(self)

if __name__ == '__main__':
    a = app()
