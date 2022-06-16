from tkinter import *
from tkinter import filedialog, Scrollbar, ttk
import pandas as pd
import sys, os

from pyparsing import col

root = Tk()
root.title('Auto Data Analyser')

open_file_f = LabelFrame(root, text='Select file', padx=5, pady=5)
open_file_f.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

columns = []

def select_file():
    global columns, select_file_l

    root.filename = filedialog.askopenfilename(initialdir='/Documents', 
        title='Select Excel File', filetypes = [('Excel files', '.xlsx .xls')])
    csv = pd.read_excel(root.filename)
    path = os.path.join(sys.path[0], 'temp/data.csv')
    csv.to_csv(path)

    select_file_l = Label(open_file_f, text=str(root.filename)+' selected', padx=5, pady =5)
    select_file_l.grid(row=1, column=0)

    columns = []
    for c in csv.columns[0:]:
        columns.append(str(c))

    refresh_checkboxes()

select_file_b = Button(open_file_f, text='Select Excel File', command=select_file)
select_file_b.grid(row=0, column=0, padx=5, pady=5)

select_file_l = Label(open_file_f, text='No file selected', padx=5, pady =5)
select_file_l.grid(row=1, column=0)


select_vars_f = LabelFrame(root, text='Select variables', padx=5, pady=5)
select_vars_f.grid(row=1, column=0, padx=10, pady=10)

select_rest_f = LabelFrame(root, text='Select result', padx=5, pady=5)
select_rest_f.grid(row=1, column=1, padx=10, pady=10)

selected_vars = {}
selected_rest = {}

def refresh_checkboxes():
    global selected_vars, selected_rest

    for widgets in select_vars_f.winfo_children():
        widgets.destroy()

    selected_vars = {}
    selected_rest = {}

    for c in columns:
        selected_vars[c] = IntVar()
        selected_rest[c] = IntVar()

        var_checkbutton = Checkbutton(select_vars_f, text=c, variable=selected_vars[c], onvalue=1, offvalue=0)
        var_checkbutton.deselect()
        var_checkbutton.pack()

        res_checkbutton = Checkbutton(select_rest_f, text=c, variable=selected_rest[c], onvalue=1, offvalue=0)
        res_checkbutton.deselect()
        res_checkbutton.pack()


confrim_f = Frame(root, padx=5, pady=5)
confrim_f.grid(row=2, column=0, columnspan=2)

preview_l = Label(confrim_f, text='No variables and results selected', padx=5, pady=5)
preview_l.grid(row=1, column=0, sticky=E)

def preview():
    global columns, selected_vars, selected_rest, preview_l

    vars_preview = 'Varibles selected: '
    rest_preview = 'Results selected: '

    for c in columns:
        if selected_vars[c].get() == 1:
            vars_preview += str(c) + '; '
        if selected_rest[c].get() == 1:
            rest_preview += str(c) + '; '

    preview_l.destroy()
    preview_l = Label(confrim_f, text=vars_preview+'\n'+rest_preview, padx=5, pady=5)
    preview_l.grid(row=1, column=0, sticky=E)


confirm_b = Button(confrim_f, text='Confirm variables and results', command=preview)
confirm_b.grid(row=0, column=0, sticky=E)

next_b = Button(confrim_f, text='Next', command=next)
next_b.grid(row=0, column=1, rowspan=2, sticky=W)



root.mainloop()