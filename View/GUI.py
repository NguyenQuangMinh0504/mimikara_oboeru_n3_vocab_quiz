import tkinter as tk
from tkinter import PhotoImage

import Setting.Load
from View.Widget.Frame.FirstFrame import FirstFrame
from View.Widget.Menu import MainMenu


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # the menu bar
        self.menu_bar = MainMenu(self)
        self.config(menu=self.menu_bar)

        # setting the select unit part
        self.frame = FirstFrame(self)
        self.frame.pack()

        # setting the logo
        logo = PhotoImage(file=Setting.Load.logo_path)
        self.iconphoto(True, logo)


