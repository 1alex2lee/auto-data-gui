from tkinter import *
import pandas as pd

def it(x, y):

    # x = pd.read_csv('temp/data_x.csv', index_col=0)
    # y = pd.read_csv('temp/data_y.csv', index_col=0)

    df = pd.DataFrame()

    x_col = x.columns[0]
    y_col = y.columns[0]

    print(x_col)

    df[x_col] = x[x_col]
    df[y_col] = y[y_col]

    df.sort_values(y_col, inplace=True)
    df = df.reset_index()

    for i in range(df.shape[0]):
        if i < df.shape[0]/2:
            df.at[i,'y_bin'] = 0
        else:
            df.at[i,'y_bin'] = 1

    # print(df)
    # df = df.drop(columns=y.columns[0])
    # df.to_csv('temp/data_y_bin.csv')

    return df