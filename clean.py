import pandas as pd
import numpy as np




def up():

    col_type = {}

    x = pd.read_csv('temp/data_x.csv', index_col=0)
    y = pd.read_csv('temp/data_y.csv', index_col=0)



    ## CLEAN X
    for x_col in x.columns:

        values = x[x_col].unique()

        # print(x_col)

        if all(isinstance(v, np.int64) for v in values) or all(isinstance(v, np.float64) for v in values):
        # try:
            
            values = values.astype(float)

            if 1 in values:
                if 0 in values:
                    if len(values) == 2:
                        # print(values.lower())
                        # print(str(x[x_col]).lower())
                        col_type[x_col] = 'binary'
                    else:
                        col_type[x_col] = 'continuous'
                else:
                    col_type[x_col] = 'continuous'

            else:
                # print(x_col+' is not a string column')
                col_type[x_col] = 'continuous'
                # pass 
        
        else:
        # except:

            x[x_col] = x[x_col].str.lower()
            values = x[x_col].unique()

            if 'yes' in values:
                if 'no' in values:
                    if len(values) == 2:
                        # print(values.lower())
                        # print(str(x[x_col]).lower())
                        x[x_col+'_bin'] = (x[x_col] == 'yes').astype(float)
                        col_type[x_col+'_bin'] = 'binary'

                        x = x.drop(columns=x_col) 

            else:
                if len(values) < 5:
                    for v in values:
                        # if v.lower() == 'yes':
                        #     x[x_col+'_bin'] = True.astype(float)
                        # elif v.lower() == 'no':
                        #     x[x_col+'_bin'] = False.astype(float)
                        # else:
                        x[x_col+'_'+str(v)] = (x[x_col] == v).astype(float)
                        # print(v+' is not a number')
                        col_type[x_col+'_'+str(v)] = 'binary'

                    x = x.drop(columns=x_col)

                else:

                    col_type[x_col] = 'too many unique values'



            
        


    ## CLEAN Y
    for y_col in y.columns:

        values = y[y_col].unique()

        if all(isinstance(v, np.int64) for v in values) or all(isinstance(v, np.float64) for v in values):

            if 1 in values:
                if 0 in values:
                    if len(values) == 2:
                        # print(values.lower())
                        # print(str(x[x_col]).lower())
                        col_type[y_col] = 'binary'
                    else:
                        col_type[y_col] = 'continuous'
                else:
                    col_type[y_col] = 'continuous'

            else:
                # print(x_col+' is not a string column')
                col_type[y_col] = 'continuous'
                # pass 
        
        else:

            y[y_col] = y[y_col].str.lower()
            values = y[y_col].unique()

            if 'yes' in values:
                if 'no' in values:
                    if len(values) == 2:
                        # print(values.lower())
                        # print(str(x[x_col]).lower())
                        y[y_col+'_bin'] = (y[y_col] == 'yes').astype(float)
                        col_type[y_col+'_bin'] = 'binary'

                        y = y.drop(columns=y_col)

            else:
                if len(values) < 5:
                    for v in values:
                        # if v.lower() == 'yes':
                        #     x[x_col+'_bin'] = True.astype(float)
                        # elif v.lower() == 'no':
                        #     x[x_col+'_bin'] = False.astype(float)
                        # else:
                        y[y_col+'_'+str(v)] = (y[y_col] == v).astype(float)
                        # print(v+' is not a number')
                        col_type[y_col+'_'+str(v)] = 'binary'

                    y = y.drop(columns=y_col)

                else:

                    col_type[y_col] = 'too many unique values'
        


    # print(x)
    # print(y)


    # x.to_csv('temp/data_x.csv')
    # y.to_csv('temp/data_y.csv')

    return x, y, col_type


# x, y, col_type = up()
# print(col_type)
# print(x, y)