from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Auto Data Analyser')

open_file_f = LabelFrame(root, text='Select file', padx=5, pady=5)
open_file_f.grid(row=0, column=0, padx=10, pady=10)

def select_file():
    root.filename = filedialog.askopenfilename(initialdir='/Documents', 
        title='Select Excel File', filetypes = [('Excel files', '.xlsx .xls')])

select_file_b = Button(open_file_f, text='Select Excel File', command=select_file)
select_file_b.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()