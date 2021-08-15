import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
k = 1
for i in range(4):
    for j in range(3):
        a = tk.Button(frame, text='Unit {}'.format(k), highlightbackground='black')
        a.grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
        k += 1
        if (i + j) % 2 == 0:
            a.config(highlightbackground='green')
root.mainloop()