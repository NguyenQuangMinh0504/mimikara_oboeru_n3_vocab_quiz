
from tkinter import PhotoImage
from Widget.Frame import *
from Widget.Status import ActiveStatus as c
from Widget.Menu import MainMenu
from Widget.Sound import Sound
from Widget.Result import Result


class Application(tk.Tk):



    #

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # the menu bar
        self.menu_bar = MainMenu(self)
        self.config(menu=self.menu_bar)

        # setting the select unit part

        self.frame = FirstFrame(self)
        self.frame.pack()

        # setting the logo
        logo = PhotoImage(file="../Assets/Image/app_icon-2.gif")
        self.iconphoto(True, logo)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # self.wrong_ans = []


if __name__ == '__main__':
    app = Application()
    app.mainloop()

