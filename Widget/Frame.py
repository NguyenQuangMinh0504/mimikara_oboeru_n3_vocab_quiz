import tkinter as tk
from tkinter import ttk


class UnitSelectionFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text='Unit').grid(row=0, column=0)
        self.unit_select_spin_box = ttk.Combobox(self, textvariable=tk.StringVar(), values=list(range(1, 12)))
        self.unit_select_spin_box.grid(row=0, column=1)
        self.select_unit_button = ttk.Button(self, text='Select')
        self.select_unit_button.grid(row=0, column=2)

