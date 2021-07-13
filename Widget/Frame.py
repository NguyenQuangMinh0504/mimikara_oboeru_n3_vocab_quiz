import tkinter as tk
from tkinter import ttk


class UnitSelectionFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        ttk.Label(self, text='Unit').grid(row=0, column=0)
        self.unit_select_spin_box = ttk.Combobox(self, textvariable=tk.StringVar(), values=list(range(1, 12)))
        self.unit_select_spin_box.grid(row=0, column=1)
        self.select_unit_button = ttk.Button(self, text='Select')
        self.select_unit_button.grid(row=0, column=2)


class LabelInputFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        ttk.Label(self, text='Kanji').grid(row=0, column=0, sticky=tk.W, padx=5)
        self.kanji_input = ttk.Entry(self)
        self.kanji_input.grid(row=1, column=0)
        self.kanji_input.config(validate='all',
                                validatecommand=(parent.register(parent.validate), '%d'))
        self.kanji_input.bind('<Return>', parent.handle)

        ttk.Label(self, text='Spelling').grid(row=0, column=1, sticky=tk.W, padx=5)
        self.spelling_input = ttk.Entry(self)
        self.spelling_input.grid(row=1, column=1)
        self.spelling_input.config(validate='all',
                                   validatecommand=(parent.register(parent.validate), '%d'))
        self.spelling_input.bind('<Return>', parent.handle)

        self.button = tk.Button(self, text='Check', command=parent.handle)
        self.button.grid(row=1, column=2)
