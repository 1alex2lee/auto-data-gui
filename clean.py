import pandas as pd

x = pd.read_csv('temp/data_x.csv', index_col=0)
y = pd.read_csv('temp/data_y.csv', index_col=0)

for x_col in x.columns:
    values = x[x_col].unique()
    for v in values:
        if type(v) == int or float:
            print('number')
        else:
            print('not number')
            x[v] = x[x_col] == v