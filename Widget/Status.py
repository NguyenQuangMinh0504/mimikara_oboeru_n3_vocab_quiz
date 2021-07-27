import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime


class ActiveStatus(tk.Toplevel):
    """Show the active day of status"""

    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.day_list = [['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']]
        self.this_month = datetime.today().month
        self.this_year = datetime.today().year
        self.this_day = datetime.today().date()
        self.day_list.extend(calendar.monthcalendar(self.this_year, self.this_month))

        title_frame = ttk.Frame(self)
        title_frame.pack()
        self.previous_button = ttk.Button(title_frame, text='Previous', command=self._previous)
        self.previous_button.grid(row=0, column=0, padx=20)
        self.next_button = ttk.Button(title_frame, text='Next', command=self._next)
        self.next_button.grid(row=0, column=2, padx=20)
        self.month_title = ttk.Label(title_frame, text=datetime.strftime(datetime.today(), '%Y %B'),
                                     font=('TkDefaultFont', 30))
        self.month_title.grid(row=0, column=1)

        self.calendar_frame = ttk.Frame(self, borderwidth=1, relief='solid')
        self.calendar_frame.pack(padx=20, pady=20)
        self._set_calendar()

    @staticmethod
    def add_active_day():
        active_day_list = ActiveStatus.get_active_day()
        with open('../mimikara_oboeru_n3_vocab_quiz/Data/Status/user_status.txt', 'a') as f:
            if len(active_day_list) == 0:
                f.write('\n' + datetime.today().strftime('%Y-%m-%d'))
            elif datetime.today().strftime('%Y-%m-%d') != active_day_list[-1]:
                f.write('\n' + datetime.today().strftime('%Y-%m-%d'))

    @staticmethod
    def get_active_day():
        with open('../mimikara_oboeru_n3_vocab_quiz/Data/Status/user_status.txt', 'r') as f:
            active_day = [i.rstrip() for i in f.readlines()]
            return active_day

    def _previous(self):
        self._clear_frame()

        if self.this_month == 1:
            self.this_year -= 1
            self.this_month = 12
        else:
            self.this_month -= 1
        self.day_list = [['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']]
        self.day_list.extend(calendar.monthcalendar(self.this_year, self.this_month))
        self._set_calendar()
        self.month_title['text'] = datetime.strftime(
            datetime.strptime(str(self.this_year)+'-'+str(self.this_month), '%Y-%m'), '%Y %B')

    def _next(self):
        self._clear_frame()
        if self.this_month == 12:
            self.this_year += 1
            self.this_month = 1
        else:
            self.this_month += 1
        self.day_list = [['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']]
        self.day_list.extend(calendar.monthcalendar(self.this_year, self.this_month))
        self._set_calendar()
        self.month_title['text'] = datetime.strftime(
            datetime.strptime(str(self.this_year) + '-' + str(self.this_month), '%Y-%m'), '%Y %B')

    def _clear_frame(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

    def _set_calendar(self):
        for i in range(len(self.day_list)):
            for j in range(7):
                if self.day_list[i][j] != 0:
                    if i == 0:
                        e = ttk.Label(self.calendar_frame, width=3, text=self.day_list[i][j], foreground='black')
                        e.grid(row=0, column=j, padx=5, pady=5, sticky=tk.E)
                    else:
                        e = ttk.Label(self.calendar_frame, width=3, text=self.day_list[i][j], foreground='red')
                        e.grid(row=i, column=j, padx=5, pady=5, sticky=tk.E)
                        # highlight active days
                        if datetime.strftime(
                                datetime.strptime('{}-{}-{}'.format(self.this_year, self.this_month, self.day_list[i][j]),
                                                  '%Y-%m-%d'), '%Y-%m-%d') in self.get_active_day():
                            e.config(foreground='green', font='TkDefaultFont 12 bold')
                        # highlight today
                        if datetime.strftime(
                                datetime.strptime(
                                    '{}-{}-{}'.format(self.this_year, self.this_month, self.day_list[i][j]),
                                    '%Y-%m-%d'), '%Y-%m-%d') == datetime.today().strftime('%Y-%m-%d'):
                            e.config(font='TkDefaultFont 15 bold', relief=tk.GROOVE)
