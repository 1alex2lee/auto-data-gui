from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math, frames, y_bin, clean

def show():

    clean.up()

    root = Tk()
    root.title('Thresholds')

    frame = frames.ScrollableFrame(root)

    Label(root, 
        text="The result is split into high and low categories, denoted with 1 or 0.\nThe split is done with its median.\nEach variable's value is shown for the high or low result."
        ).pack()

    x = pd.read_csv('temp/data_x.csv', index_col=0)
    y = pd.read_csv('temp/data_y.csv', index_col=0)

    y_bin.bin_it()

    for y_col in y.columns:
        df_y = pd.DataFrame()
        df_y[y_col] = y[y_col]
        df_y.sort_values(y_col, inplace=True)
        threshold = df_y.at[math.floor(df_y.shape[0]/2), y_col]
        Label(frame.scrollable_frame, text='For '+y_col+', threshold = '+str(round(threshold,2))).pack()

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
            chart_type = FigureCanvasTkAgg(figure, frame.scrollable_frame)
            chart_type.get_tk_widget().pack(padx=5, pady=5)
            ax.set_title('Threshold of '+x_col+' on '+y_col, fontsize=10)
            ax.set_xlabel(x_col, fontsize=10)
            ax.set_ylabel(y_col+' (1=high, 2=low)', fontsize=10)
            df.plot.scatter(x=x_col, y='y_bin', ax=ax, legend=False)
            
    frame.pack()

    root.mainloop()

# show_thresholds()