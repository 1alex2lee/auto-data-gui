from tkinter import *
from tkinter import filedialog, Scrollbar, ttk
import pandas as pd
import sys, os

root = Tk()
root.title('Auto Data Analyser')

open_file_f = LabelFrame(root, text='Select and Preview file', padx=5, pady=5)
open_file_f.grid(row=0, column=0, padx=10, pady=10)

def select_file():
    global preview_table
    root.filename = filedialog.askopenfilename(initialdir='/Documents', 
        title='Select Excel File', filetypes = [('Excel files', '.xlsx .xls')])
    csv = pd.read_excel(root.filename)
    path = os.path.join(sys.path[0], 'temp/data.csv')
    csv.to_csv(path)

    columns = []
    for c in csv.columns[0:]:
        columns.append(str(c))

    preview_table['columns'] = columns

    preview_table.column('#0', width=0,  stretch=NO)
    preview_table.heading('#0',text='',anchor=CENTER)

    for c in columns:
        # preview_table.column(c,anchor=CENTER, width=10)
        preview_table.heading(c,text=c,anchor=CENTER)

    for k in range(11):
        values = []
        for c in columns:
            values.append(csv.iloc[k][c])
        print(tuple(values))
        preview_table.insert(parent='',index='end',iid=k,text='', values = values)

    # my_table.pack(expand = True)    




select_file_b = Button(open_file_f, text='Select Excel File', command=select_file)
select_file_b.grid(row=0, column=0, padx=5, pady=5)

xscroll = Scrollbar(open_file_f, orient='horizontal')
xscroll.grid(row=2, column=0, sticky='ew')

preview_table = ttk.Treeview(open_file_f, xscrollcommand=xscroll.set)
preview_table.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()