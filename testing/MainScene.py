import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
k = 1

data = {"Unit 1": False, "Unit 2": False, "Unit 3": False, "Unit 4": False, "Unit 5": False, "Unit 6": False,
        "Unit 7": False, "Unit 8": False, "Unit 9": False, "Unit 10": False, "Unit 11": False, "Unit 12": False}

for i in range(4):
    for j in range(3):
        label = "Unit {}".format(k)
        a = tk.Button(frame, text=label)
        a.grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
        if data[label]:
            a.config(highlightbackground='green')
        else:
            a.config(highlightbackground='red')
        k += 1
root.mainloop()
