import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime


class Calendar(tk.Toplevel):

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        day_list = [['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']]
        day_list.extend(calendar.monthcalendar(2021, 7))
        total_rows = len(day_list)
        months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                  7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        calendar_frame = ttk.Frame(self, borderwidth=1, relief='solid')
        ttk.Label(self, text='2021 ' + months.get(datetime.today().month), font=('TkDefaultFont', 30)).pack()
        calendar_frame.pack(padx=20, pady=20)
        for j in range(7):
            e = ttk.Label(calendar_frame, width=3, foreground='black')
            e.grid(row=0, column=j, padx=5, pady=5, sticky=tk.E)
            e['text'] = day_list[0][j]

        for i in range(1, total_rows):
            for j in range(7):
                e = ttk.Label(calendar_frame, width=3, foreground='red')
                e.grid(row=i, column=j, padx=5, pady=5, sticky=tk.E)
                if day_list[i][j] != 0:
                    e['text'] = day_list[i][j]
                    if datetime.strftime(datetime.strptime('2021-07-' + str(e['text']), '%Y-%m-%d'), '%Y-%m-%d') \
                            in self.get_active_day():
                        e.config(foreground='green')

    @staticmethod
    def add_active_day():
        with open('../JapaneseQuizProject/Data/Status/user_status.txt', 'a') as f:
            f.write(datetime.today().strftime('%Y-%m-%d'))

    @staticmethod
    def get_active_day():
        with open('../JapaneseQuizProject/Data/Status/user_status.txt', 'r') as f:
            active_day = [i.rstrip() for i in f.readlines()]
            return active_day





