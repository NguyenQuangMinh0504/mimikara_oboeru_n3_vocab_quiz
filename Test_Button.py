import pandas as pd
import tkinter as tk
import tkinter.font as font
root = tk.Tk()
x = pd.read_csv('Dataset/data1.csv')
print(len(x))


def on_save():
    label['text'] = x.loc[9][0]


button = tk.Button(root, text='CLick me', command=on_save)
button.pack()
label = tk.Label(root, text=x.loc[0][0], font=font.Font(size=30))
label.pack()
root.mainloop()
