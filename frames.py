import tkinter as tk
from tkinter import ttk

from pyparsing import col

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        canvas.config(height=500, width=400)
        x_scroll = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        y_scroll = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        canvas.grid(row=0, column=0)
        y_scroll.grid(row=0, column=1)
        x_scroll.grid(row=1, column=0)