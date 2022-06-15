from tkinter import *
from tkinter import filedialog, Scrollbar, ttk
import pandas as pd
import sys, os

from pyparsing import col

root = Tk()
root.title('Auto Data Analyser')

open_file_f = LabelFrame(root, text='Select file', padx=5, pady=5)
open_file_f.grid(row=0, column=0, padx=10, pady=10)

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

select_file_b = Button(open_file_f, text='Select Excel File', command=select_file)
select_file_b.grid(row=0, column=0, padx=5, pady=5)

select_file_l = Label(open_file_f, text='No file selected', padx=5, pady =5)
select_file_l.grid(row=1, column=0)


select_vars_f = LabelFrame(root, text='Select variables', padx=5, pady=5)
select_vars_f.grid(row=1, column=0, padx=10, pady=10)

for c in columns:
    checkbutton = Checkbutton(select_vars_f, text=c)
    checkbutton.deselect()
    checkbutton.pack()


root.mainloop()