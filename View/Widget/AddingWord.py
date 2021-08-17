import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import csv


class VocabularyInput(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        ttk.Label(self, text='Mimikara Oboeru Vocabulary Input', font=('TkDefaultFont', 30)).\
            grid(row=0, sticky=tk.W+tk.E, padx=20)
        self.geometry('+450+300')

        data_input = ttk.LabelFrame(self)
        data_input.grid(row=1, ipady=30)

        # adding word label and word input
        ttk.Label(data_input, text='Word').grid(row=0, column=0, sticky=tk.W+tk.E, padx=20)
        self.word_input = tk.StringVar()
        self.word_entry = ttk.Entry(data_input, textvariable=self.word_input)
        self.word_entry.grid(row=1, column=0, sticky=tk.W+tk.E, padx=20)
        # adding meaning label and meaning input
        ttk.Label(data_input, text='Meaning').grid(row=0, column=1, sticky=tk.W + tk.E, padx=20)
        self.meaning_input = tk.StringVar()
        ttk.Entry(data_input, textvariable=self.meaning_input).grid(row=1, column=1, sticky=tk.W+tk.E, padx=20)

        # adding spelling label and spelling input
        ttk.Label(data_input, text='Spelling').grid(row=2, column=0, sticky=tk.W+tk.E, padx=20)
        self.spelling_input = tk.StringVar()
        ttk.Entry(data_input, textvariable=self.spelling_input).grid(row=3, column=0, sticky=tk.W+tk.E, padx=20)

        # adding kanji label and kanji input
        ttk.Label(data_input, text='Kanji').grid(row=2, column=1, sticky=tk.W+tk.E, padx=20)
        self.kanji_input = tk.StringVar()
        ttk.Entry(data_input, textvariable=self.kanji_input).grid(row=3, column=1, sticky=tk.W+tk.E, padx=20)

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

        if any([not self.word_input.get(),
                not self.spelling_input.get(),
                not self.meaning_input.get(),
                not self.kanji_input.get()]):
            VocabularyInput._error_message()
            return None

        new_file = not os.path.exists('./Data/Dictionary/unit6.csv')
        with open('./Data/Dictionary/unit6.csv', 'a') as f:
            csv_writer = csv.DictWriter(f, fieldnames=['Word', 'Meaning', 'Spelling', 'Kanji'])
            if new_file:
                csv_writer.writeheader()
            csv_writer.writerow(data)
            self.status.set('Status: Success, the word {} had been add to dictionary'.format(self.word_input.get()))

        self.word_input.set('')
        self.spelling_input.set('')
        self.meaning_input.set('')
        self.kanji_input.set('')
        self.word_entry.focus_set()

    @staticmethod
    def _error_message():
        title = 'Error'
        message = 'Empty entry. Please check again!'
        messagebox.showerror(title=title, message=message)
