from tkinter import *
import pandas as pd
import frames, y_bin
from sklearn.linear_model import LogisticRegression as logreg
from sklearn.metrics import accuracy_score

def show():

    root = Tk()
    root.title('Logistic Regression')

    frame = frames.ScrollableFrame(root)

    Label(root, 
        text="Each variable is fitted to a Logsitics Regression model to predict the result.\nTheir accuracies are shown."
        ).pack()

    y_bin.bin_it()

    df = pd.read_csv('temp/data_y_bin.csv', index_col=0)
    y_col = df.columns[-2]
    x = df.drop(columns=['y_bin','index',y_col])
    y = df['y_bin']
    # print(x)
    # print(y)

    for x_col in x.columns:
        X = x[x_col].values.reshape(-1,1)
        Y = y.values.reshape(-1,1)
        # print(X)
        # print(Y)

        mylr = logreg()
        mylr.fit(X, Y)

        print('Accuracy of '+x_col+' on '+y_col+' is '+str(accuracy_score(Y,  mylr.predict(X))))

        Label(frame.scrollable_frame, text='Accuracy of '+x_col+' on '+y_col+' is '+str(round(accuracy_score(Y,  mylr.predict(X)), 2))).pack()

        # model_summary = ModelSummary.ModelSummary(mylr, X, Y)
        # model_summary.get_summary()


    frame.pack()

    root.mainloop()
