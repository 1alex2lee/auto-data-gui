from sklearn import tree
from sklearn.metrics import accuracy_score
import pandas as pd
import clean, graphviz
from tkinter import *
from PIL import Image, ImageTk


def show(x, y):

    root = Tk()
    root.title('Decision Tree')

    # x, y = clean.up()

    # x = pd.read_csv('temp/data_x.csv', index_col=0)
    # y = pd.read_csv('temp/data_y.csv', index_col=0)

    dt = tree.DecisionTreeClassifier(max_depth=5, min_impurity_decrease=0.01)
    dt.fit(x, y)
    # print('Accuracy = {}'.format(accuracy_score(y, dt.predict(x))))


    dot_data = tree.export_graphviz(dt, out_file=None) 
    graph = graphviz.Source(dot_data) 

    predictors = x.columns
    dot_data = tree.export_graphviz(dt, out_file=None,
                                    feature_names = predictors,
                                    class_names = ('Negative', 'Positive'),
                                    filled = True, rounded = True,
                                    special_characters = True)
    graph = graphviz.Source(dot_data)  
    graph

    graph.format = 'png'
    graph.render('temp/decisiontree')


    Label(root, 
        text="A decision tree uses a selection algorithm to select variables in a predictive model."
        ).pack()

    image = Image.open('temp/decisiontree.png')
    display = ImageTk.PhotoImage(image)
    Label(root, image=display).pack()

    root.mainloop()