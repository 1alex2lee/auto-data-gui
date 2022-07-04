from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math, frames, bin, clean

from sklearn.utils import column_or_1d

from pyparsing import col

def show(x, y, col_type):

    # clean.up()

    root = Tk()
    root.title('Thresholds')

    frame = frames.ScrollableFrame(root)

    Label(root, 
        text="The result is split into high and low categories, denoted with 1 or 0.\nThe split is done with its median.\nEach variable's value is shown for the high or low result."
        ).pack()

    # x = pd.read_csv('temp/data_x.csv', index_col=0)
    # y = pd.read_csv('temp/data_y.csv', index_col=0)

    # y_bin.bin_it()

    # print(x)
    # print(y)
    # print(col_type)

    for y_col in y.columns:

        if col_type[y_col] == 'binary':

            # print('Y is binary')

            for x_col in x.columns:

                if col_type[x_col] == 'continuous':

                    # print('x is continuous')

                    df = pd.DataFrame()
                    df['x'] = x[x_col]
                    df['y'] = y[y_col]   

                    figure = plt.Figure(figsize=(4,4), dpi=90)
                    ax = figure.add_subplot(111)
                    chart_type = FigureCanvasTkAgg(figure, frame.scrollable_frame)
                    chart_type.get_tk_widget().pack(padx=5, pady=5)
                    ax.set_title('Threshold of '+x_col+' on '+y_col, fontsize=10)
                    ax.set_xlabel(x_col, fontsize=10)
                    ax.set_ylabel(y_col+' (1=high, 2=low)', fontsize=10)
                    # print(df)
                    df.plot.scatter(x='x', y='y', ax=ax, legend=False)

                elif col_type[x_col] == 'binary':

                    # print('X is binary')

                    table = Frame(root)

                    Label(table, text=x_col+' true').grid(row=0, column=1)
                    Label(table, text=x_col+' false').grid(row=0, column=2)
                    Label(table, text=y_col+' true').grid(row=1, column=0)
                    Label(table, text=y_col+' false').grid(row=2, column=0)

                    ff = ft = tf = tt = 0

                    for i in range(len(x)):

                        # print(i)

                        if x.at[i, x_col] == 0 and y.at[i, y_col] == 0:
                            ff += 1
                        elif x.at[i, x_col] == 1 and y.at[i, y_col] == 0:
                            tf += 1
                        elif x.at[i, x_col] == 0 and y.at[i, y_col] == 1:
                            ft += 1
                        elif x.at[i, x_col] == 1 and y.at[i, y_col] == 1:
                            tt += 1
                        
                        # print(str(ff)+' '+str(tf)+' '+str(ft)+' '+str(tt))
                    
                    Label(table, text=ff).grid(row=2, column=2)
                    Label(table, text=tf).grid(row=2, column=1)
                    Label(table, text=ft).grid(row=1, column=2)
                    Label(table, text=tt).grid(row=1, column=1)

                    table.pack(padx=5, pady=5)



        if col_type[y_col] == 'continuous':

            # print('Y is binary')

            # df_y = pd.DataFrame()
            # df_y[y_col] = y[y_col]
            # df_y.sort_values(y_col, inplace=True)
            # threshold = df_y.at[math.floor(df_y.shape[0]/2), y_col]

            # Label(frame.scrollable_frame, text='For '+y_col+', threshold = '+str(round(threshold,2))).pack()

            for x_col in x.columns:

                if col_type[x_col] == 'continuous':

                    frame = Frame(root)

                    def refresh(v):
                        Label(frame, text='y threshold is '+str(y_threshold.get())).grid(row=2, column=0)
                        Label(frame, text='x threshold is '+str(x_threshold.get())).grid(row=2, column=1)

                    # print(y[y_col].min())

                    y_threshold = Scale(frame, from_=y[y_col].max(), to=y[y_col].min(), resolution=(y[y_col].max()-y[y_col].min())/10, orient='vertical', command=refresh, length=350)
                    y_threshold.grid(row=0, column=0)
                    x_threshold = Scale(frame, from_=x[x_col].min(), to=x[x_col].max(), resolution=(x[x_col].max()-x[x_col].min())/10, orient='horizontal', command=refresh, length=350)
                    x_threshold.grid(row=1, column=1)

                    Label(frame, text='y threshold is 0').grid(row=2, column=0)
                    Label(frame, text='x threshold is 0').grid(row=2, column=1)



                    # print('x is continuous')

                    # df = bin.it(x, y)

                    df = pd.DataFrame()

                    df[x_col] = x[x_col]
                    df[y_col] = y[y_col]

                    figure = plt.Figure(figsize=(4,4), dpi=100)
                    ax = figure.add_subplot(111)
                    chart_type = FigureCanvasTkAgg(figure, frame)
                    chart_type.get_tk_widget().grid(row=0, column=1, padx=5, pady=5)
                    ax.set_title('Threshold of '+x_col+' on '+y_col, fontsize=10)
                    # print(df)
                    df.plot.scatter(x=x_col, y=y_col, ax=ax, legend=False)
                    # ax.set_xlabel(x_col, fontsize=10)
                    # ax.set_ylabel(df.columns[1]+' (0=low, 1=high)', fontsize=10)

            
                    frame.pack()

    root.mainloop()

x, y, col_type = clean.up()
show(x, y, col_type)