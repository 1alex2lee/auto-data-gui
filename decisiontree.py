from sklearn import tree
from sklearn.metrics import accuracy_score
import graphviz, clean
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from matplotlib import pyplot as plt


def show(x, y):
    global max_d, min_i_d

    root = Toplevel()
    root.title('Decision Tree')

    Label(root, 
    text="A decision tree uses a selection algorithm to select variables for a predictive model.\nIt requires 2 parameters as below. Feel free to change these parameters."
    ).grid(row=0, column=0, columnspan=3)

    Label(root, text="Max depth (integer > 2, default = 5)").grid(row=1, column=0)
    Label(root, text="Min impurity increase (0.1-0.001, default = 0.01)").grid(row=1, column=1)

    max_d = Entry(root)
    max_d.insert(END, '5')
    max_d.grid(row=2, column=0)

    min_i_d = Entry(root)
    min_i_d.insert(END, '0.01')
    min_i_d.grid(row=2, column=1)


    tree_f = Frame(root)
    tree_f.grid(row=3, column=0, columnspan=3)


    def create_tree(event=None):

        for widgets in tree_f.winfo_children():
            widgets.destroy()

        # x, y = clean.up()

        # x = pd.read_csv('temp/data_x.csv', index_col=0)
        # y = pd.read_csv('temp/data_y.csv', index_col=0)

        try:
            max_depth = int(max_d.get())
            min_i_decrease = float(min_i_d.get())
        except:
            messagebox.showerror('Error', "You didn't input a number.")
            return

        try:
            dt = tree.DecisionTreeClassifier(
                max_depth=max_depth, 
                min_impurity_decrease=min_i_decrease)
            dt.fit(x, y)
            # print('Accuracy = {}'.format(accuracy_score(y, dt.predict(x))))
        except:
            messagebox.showerror('Error', "Parameters out of range.")
            return

        # dot_data = tree.export_graphviz(dt, out_file=None) 
        # graph = graphviz.Source(dot_data) 

        predictors = x.columns

        # dot_data = tree.export_graphviz(dt, out_file=None,
        #                                 feature_names = predictors,
        #                                 class_names = ('Negative', 'Positive'),
        #                                 filled = True, rounded = True,
        #                                 special_characters = True)
        # graph = graphviz.Source(dot_data)  
        # graph

        # graph.format = 'png'
        # graph.render('temp/decisiontree')


        fig = plt.figure(figsize=(12,12))
        _ = tree.plot_tree(dt, 
                   feature_names=predictors,
                   class_names=('Negative', 'Positive'),
                   filled=True, rounded=True)
        fig.savefig("temp/decisiontree.png")


        image = Image.open('temp/decisiontree.png')
        display = ImageTk.PhotoImage(image)
        photo_label = Label(tree_f, image=display)
        photo_label.image = display
        photo_label.pack()



    root.bind('<Return>', create_tree)

    Button(root, text='Create Tree', command=create_tree).grid(row=1, column=2)


    def help():
        root = Tk()
        root.title('About Decision Trees')




    Button(root, text='Help', command=help).grid(row=2, column=2)


    root.mainloop()


x, y = clean.up()
show(x, y)