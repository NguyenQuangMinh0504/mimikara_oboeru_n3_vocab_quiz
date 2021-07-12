from tkinter import Menu, BooleanVar, messagebox
from Widget.Status import ActiveStatus


class MainMenu(Menu):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        profile_menu = Menu(self)
        profile_menu.add_command(label='Status', command=self.show_status)
        self.add_cascade(label='Profile', menu=profile_menu)

        setting_menu = Menu(self)
        self.sound = BooleanVar(value=True)
        setting_menu.add_checkbutton(label='Sound', variable=self.sound)
        self.add_cascade(label='Setting', menu=setting_menu)

        help_menu = Menu(self)
        self.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='About...', command=self.show_about)

    def show_status(self):
        ActiveStatus(root=self)

    def show_about(self):
        about_message = "Mimikara Oboeru App"
        about_detail = ("Tạo bởi Nguyễn Quang Minh\n",
                        "Gặp lỗi vui lòng liên hệ ngquangminh05042001@gmail.com")
        messagebox.showinfo(title="About", message=about_message, detail=about_detail)

