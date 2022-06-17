from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from pyparsing import col

def show_graphs():

    root = Tk()
    root.title('Graphs')

    x = pd.read_csv('temp/data_x.csv', index_col=0)
    y = pd.read_csv('temp/data_y.csv', index_col=0)

    for y_col in y.columns:
        figure = plt.Figure(figsize=(5,5), dpi=80)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, root)
        chart_type.get_tk_widget().pack()
        ax.set_title('Variables againast '+y_col, fontsize=10)
        for x_col in x.columns:
            df = pd.DataFrame()
            df[x_col] = x[x_col]
            df[y_col] = y[y_col]
            df.sort_values(x_col, inplace=True)
            df.plot(x=x_col, y=y_col, ax=ax, label=x_col, xlabel='Variables', ylabel=y_col)
            ax.legend(loc='center right', fontsize=8)


    root.mainloop()

