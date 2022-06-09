from tkinter import filedialog as fd

import pandas as pd
import os
import sys

def open_file():
    filename = fd.askopenfilename(
        title = 'Open a file',
        initialdir = '/',
        filetypes = [('Excel files', '.xlsx .xls')])
    
    # filename = '/Users/alexlee/Documents/Auto Data GUI/auto-data-gui'

    file = pd.read_excel(filename)
    path = os.path.join(sys.path[0], "temp/data.csv")
    file.to_csv(path)