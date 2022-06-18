from tkinter import *
import pandas as pd

def bin_it():

    x = pd.read_csv('temp/data_x.csv', index_col=0)
    y = pd.read_csv('temp/data_y.csv', index_col=0)

    df = pd.DataFrame()
    for x_col in x.columns:
        df[x_col] = x[x_col]
    df[y.columns[0]] = y[y.columns[0]]
    df.sort_values(y.columns[0], inplace=True)
    df = df.reset_index()
    for i in range(df.shape[0]):
        if i < df.shape[0]/2:
            df.at[i,'y_bin'] = 0
        else:
            df.at[i,'y_bin'] = 1
    # print(df)
    # df = df.drop(columns=y.columns[0])
    df.to_csv('temp/data_y_bin.csv')