
from tkinter import PhotoImage
from Widget.Frame import *
from Widget.Menu import MainMenu


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
        logo = PhotoImage(file="../Assets/Image/app_icon-2.gif")
        self.iconphoto(True, logo)




if __name__ == '__main__':
    app = Application()
    app.mainloop()
