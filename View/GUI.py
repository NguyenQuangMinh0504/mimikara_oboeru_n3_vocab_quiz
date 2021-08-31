import tkinter as tk
import Setting.Load
from View.Widget.Frame.FirstFrame import FirstFrame
from View.Widget.Menu import MainMenu


class Application(tk.Tk):
    """
    Main Application
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set up menu bar
        self.menu_bar = MainMenu(self)
        self.config(menu=self.menu_bar)

        # set up first frame
        self.frame = FirstFrame(self)
        self.frame.pack()

        # set up the logo
        logo = tk.PhotoImage(file=Setting.Load.logo_path)
        self.iconphoto(True, logo)


