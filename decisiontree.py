from sklearn import tree
from sklearn.metrics import accuracy_score
import pandas as pd
import clean, graphviz

x, y = clean.up()

# x = pd.read_csv('temp/data_x.csv', index_col=0)
# y = pd.read_csv('temp/data_y.csv', index_col=0)

dt = tree.DecisionTreeClassifier(max_depth=4, min_impurity_decrease=0.03)
dt.fit(x, y)
print('Accuracy = {}'.format(accuracy_score(y, dt.predict(x))))


import sklearn.tree as tree
import graphviz
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