import tkinter as tk
from tkinter import ttk
import os
import csv


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ttk.Label(self, text='Mimikara Oboeru Vocabulary Input', font=('TkDefaultFont', 30)).\
            grid(row=0, sticky=tk.W+tk.E, padx=20)
        self.geometry('+450+300')

        data_input = ttk.LabelFrame(self)
        data_input.grid(row=1, ipady=30)

        # adding word label and word input
        self.word_label = ttk.Label(data_input, text='Word').grid(row=0, column=0, sticky=tk.W+tk.E, padx=20)
        self.word_input = ttk.Entry(data_input)
        self.word_input.grid(row=1, column=0, sticky=tk.W+tk.E, padx=20)

        # adding meaning label and meaning input
        self.meaning_label = ttk.Label(data_input, text='Meaning').grid(row=0, column=1, sticky=tk.W + tk.E, padx=20)
        self.meaning_input = ttk.Entry(data_input)
        self.meaning_input.grid(row=1, column=1, sticky=tk.W + tk.E, padx=20)

        # adding spelling label and spelling input
        self.spelling_label = ttk.Label(data_input, text='Spelling').grid(row=2, column=0, sticky=tk.W+tk.E, padx=20)
        self.spelling_input = ttk.Entry(data_input)
        self.spelling_input.grid(row=3, column=0, sticky=tk.W+tk.E, padx=20)

        # adding kanji label and kanji input
        self.kanji_label = ttk.Label(data_input, text='Kanji').grid(row=2, column=1, sticky=tk.W+tk.E, padx=20)
        self.kanji_input = ttk.Entry(data_input)
        self.kanji_input.grid(row=3, column=1, sticky=tk.W+tk.E, padx=20)

        # adding save button
        self.save_button = ttk.Button(self, text='Save', command=self.on_save)
        self.save_button.grid(sticky=tk.E, row=4, padx=10, pady=10)

        # adding status
        self.status = tk.StringVar()
        self.status.set('Status:')
        self.status_bar = ttk.Label(self, textvariable=self.status)
        self.status_bar.grid(sticky=tk.W, row=3, padx=10, pady=10)

    def on_save(self):
        data = {'Word': self.word_input.get(), 'Meaning': self.meaning_input.get(), 'Spelling':
                self.spelling_input.get(), 'Kanji': self.kanji_input.get()}
        new_file = not os.path.exists('../Dataset/data4.csv')
        with open('../Dataset/data4.csv', 'a') as f:
            csv_writer = csv.DictWriter(f, fieldnames=['Word', 'Meaning', 'Spelling', 'Kanji'])
            if new_file:
                csv_writer.writeheader()
            csv_writer.writerow(data)
            self.status.set('Status: Success, the word {} had been add to dictionary'.format(self.word_input.get()))


if __name__ == '__main__':
    app = Application()
    app.mainloop()
