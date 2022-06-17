from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
from pyparsing import col

root = Tk()
root.title('Thresholds')

canvas = Canvas(root,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))

vbar = Scrollbar(root, orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=canvas.yview)

canvas.config(width=300,height=300)
canvas.config(yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

x = pd.read_csv('temp/data_x.csv', index_col=0)
y = pd.read_csv('temp/data_y.csv', index_col=0)

for y_col in y.columns:
    df_y = pd.DataFrame()
    df_y[y_col] = y[y_col]
    df_y.sort_values(y_col, inplace=True)
    threshold = df_y.at[math.floor(df_y.shape[0]/2), y_col]
    Label(canvas, text='For '+y_col+', threshold = '+str(round(threshold,2))).pack()
    for x_col in x.columns:
        df = pd.DataFrame()
        df[x_col] = x[x_col]
        df[y_col] = y[y_col]   
        df.sort_values(y_col, inplace=True)
        df = df.reset_index()
        for i in range(df.shape[0]):
            if i < df.shape[0]/2:
                df.at[i,'y_bin'] = 0
            else:
                df.at[i,'y_bin'] = 1
        figure = plt.Figure(figsize=(4,4), dpi=90)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, canvas)
        chart_type.get_tk_widget().pack(padx=5, pady=5)
        ax.set_title('Threshold of '+x_col+' on '+y_col, fontsize=10)
        ax.set_xlabel(x_col, fontsize=10)
        ax.set_ylabel(y_col+' (1=high, 2=low)', fontsize=10)
        df.plot.scatter(x=x_col, y='y_bin', ax=ax, legend=False)
        



root.mainloop()


# for y_col in y.columns:
#         figure = plt.Figure(figsize=(5,5), dpi=80)
#         ax = figure.add_subplot(111)
#         chart_type = FigureCanvasTkAgg(figure, root)
#         chart_type.get_tk_widget().pack()
#         ax.set_title('Variables againast '+y_col, fontsize=10)
#         for x_col in x.columns:
#             df = pd.DataFrame()
#             df[x_col] = x[x_col]
#             df[y_col] = y[y_col]
#             df.sort_values(x_col, inplace=True)
#             df.plot(x=x_col, y=y_col, ax=ax, label=x_col, xlabel='Variables', ylabel=y_col)
#             ax.legend(loc='center right', fontsize=8)

# df.sort_values(x_col, inplace=True)