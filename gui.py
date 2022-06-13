# Copyright Alexander Lee

from msilib.schema import ListView
from select import select
import tkinter as tk
from tkinter import Scrollbar, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import pandas as pd
import os
import sys

from pyparsing import col

# from open_file import open_file


class pages(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (select_file_page, csv_page):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame('csv_page')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class select_file_page(tk.Frame):
    def __init__(self, parent, controller):

        def open_file():
            filename = fd.askopenfilename(
                title = 'Open a file',
                initialdir = '/',
                filetypes = [('Excel files', '.xlsx .xls')])

            file = pd.read_excel(filename)
            path = os.path.join(sys.path[0], 'temp/data.csv')
            file.to_csv(path)
            controller.show_frame('csv_page')

        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text = 'Select an Excel file').pack(expand = True)
        ttk.Button(self, text = 'Select File',command = open_file).pack(expand = True)

class csv_page(tk.Frame):
    def __init__(self, parent, controller):

        data = pd.read_csv('temp/data.csv')
        columns = []
        for c in data.columns[1:]:
            columns.append(str(c))

        tk.Frame.__init__(self, parent)

        table = tk.Frame()
        table.pack()

        scroll = Scrollbar(table, orient = 'horizontal')
        scroll.pack(side = tk.BOTTOM, fill = tk.X)

        my_table = ttk.Treeview(table, xscrollcommand = scroll.set)
        my_table.pack()

        scroll.config(command = my_table.xview)

        my_table['columns'] = columns

        my_table.column('#0', width=0,  stretch=tk.NO)
        my_table.heading('#0',text='',anchor=tk.CENTER)

        for c in columns:
            my_table.column(c,anchor=tk.CENTER, width=80)
            my_table.heading(c,text=c,anchor=tk.CENTER)

        for k in range(11):
            values = []
            for c in columns:
                values.append(data.iloc[k][c])
            print(tuple(values))
            my_table.insert(parent='',index='end',iid=k,text='', values = values)

        my_table.pack()

        self.controller = controller
        tk.Label(self, text = 'Confirm File').pack(expand = True)
        ttk.Button(self, text = 'Confirm',command = controller.show_frame('select_columns_page')).pack(expand = True)

class select_columns_page(tk.Frame):
    def __init__(self, parent, controller):

        data = pd.read_csv('temp/data.csv')
        columns = []
        for c in data.columns[1:]:
            columns.append(str(c))

        columns_var = tk.StringVar(value = columns)

        tk.listbox(self, listvariable = columns_var, heoght = 6, selectmode = 'extended').pack()


if __name__ == '__main__':
    root = pages()
    root.title('Auto Data Analyser')
    root.wm_geometry('500x500')
    root.mainloop()
