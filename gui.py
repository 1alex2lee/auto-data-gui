# Copyright Alexander Lee

from select import select
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from open_file import open_file


class pages(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (select_file_page, csv_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("select_file_page")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class select_file_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text = 'Select an Excel file').pack(expand = True)
        ttk.Button(self, text = 'Select File',command = open_file).pack(expand = True)
        ttk.Button(self, text = 'Next', command=lambda: controller.show_frame("csv_page")).pack(expand = True)

class csv_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text = 'Confirm File').pack(expand = True)
        ttk.Button(self, text = 'Confirm',command = '').pack(expand = True)


if __name__ == '__main__':
    root = pages()
    root.title('Auto Data Analyser')
    root.wm_geometry('500x500')
    root.mainloop()
