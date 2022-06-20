import pandas as pd
import numpy as np



def up():

    x = pd.read_csv('temp/data_x.csv', index_col=0)
    y = pd.read_csv('temp/data_y.csv', index_col=0)



    ## CLEAN X
    for x_col in x.columns:
        try:
            x[x_col] = x[x_col].str.lower()
            # print(x_col+' is a string column')

            values = x[x_col].unique()

            if 'yes' in values:
                if 'no' in values:
                    if len(values) == 2:
                        # print(values.lower())
                        # print(str(x[x_col]).lower())
                        x[x_col+'_bin'] = (x[x_col] == 'yes').astype(float)
            else:
                if len(values) < 6:
                    for v in values:
                        # print(type(v))
                        if type(v) == int or type(v) == float or type(v) == np.int64:
                            print(str(v)+' is a number')
                        else:
                            if v.lower() == 'yes':
                                x[x_col+'_bin'] = True.astype(float)
                            elif v.lower() == 'no':
                                x[x_col+'_bin'] = False.astype(float)
                            else:
                                x[x_col+'_'+v] = x[x_col] == v
                                # print(v+' is not a number')
            x = x.drop(columns=x_col)
        except:
            print(x_col+' is not a string column')
        


    ## CLEAN Y
    for y_col in y.columns:
        try:
            y[y_col] = y[y_col].str.lower()
            # print(x_col+' is a string column')

            values = y[y_col].unique()

            if 'yes' in values:
                if 'no' in values:
                    if len(values) == 2:
                        # print(values.lower())
                        # print(str(x[x_col]).lower())
                        y[y_col+'_bin'] = (y[y_col] == 'yes').astype(float)
            else:
                if len(values) < 6:
                    for v in values:
                        # print(type(v))
                        if type(v) == int or type(v) == float or type(v) == np.int64:
                            print(str(v)+' is a number')
                        else:
                            if v.lower() == 'yes':
                                y[y_col+'_bin'] = True.astype(float)
                            elif v.lower() == 'no':
                                y[y_col+'_bin'] = False.astype(float)
                            else:
                                y[y_col+'_'+v] = y[y_col] == v
                                # print(v+' is not a number')
            y = y.drop(columns=y_col)
        except:
            print(y_col+' is not a string column')
        


    print(x)
    print(y)


    x.to_csv('temp/data_x.csv')
    y.to_csv('temp/data_y.csv')


