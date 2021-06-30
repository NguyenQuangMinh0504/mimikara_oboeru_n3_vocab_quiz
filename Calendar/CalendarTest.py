import tkinter as tk
from tkinter import ttk
import calendar
import datetime
day_list = [['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']]
day_list.extend(calendar.monthcalendar(2021, 7))
root = tk.Tk()
root.geometry('400x250+500+200')
total_rows = len(day_list)
total_columns = len(day_list[0])
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

calendar_frame = ttk.Frame(root, borderwidth=1, relief='solid', width=550, height=400)
ttk.Label(root, text='2021 ' + months[datetime.datetime.today().month-1], font=('TkDefaultFont', 30)).pack()
calendar_frame.pack()

for i in range(total_rows):
    for j in range(total_columns):
        e = ttk.Label(calendar_frame, width=3)


        if j % 2 == 0:
            e['foreground'] = 'green'
        if i == 0:
            e['foreground'] = 'black'

        e.grid(row=i, column=j, padx=5, pady=5, sticky=tk.E)
        e.grid_propagate(0)
        if day_list[i][j] != 0:
            e['text'] = day_list[i][j]

root.mainloop()
