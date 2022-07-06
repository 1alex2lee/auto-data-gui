from tkinter import *
from tkinter import messagebox
import tensorflow as tf
from keras.models import Sequential
import pandas as pd
from keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import clean

# mnist = tf.keras.datasets.mnist

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0


def train(x, y, layers, epoch, split):

    try:
        layers = int(layers)
        epoch = int(epoch)
        split = float(split)
        if layers < 3:
            messagebox.showerror('Error', "Input incorrect.")
        if split >= 1 or split <= 0:
            messagebox.showerror('Error', "Input incorrect.")
    except:
        messagebox.showerror('Error', "Input incorrect.")
        return

    try:

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=split, random_state=42)
        
        scaler = StandardScaler().fit(X_train)
        X_train = scaler.transform(X_train)
        # X_test = scaler.transform(X_test)


        model = Sequential()
        model.add(Dense(8, activation='relu', input_shape=(1,)))

        for l in range (layers-2):
            model.add(Dense(8, activation='relu'))

        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy',
        optimizer='sgd',
        metrics=['accuracy'])
        model.fit(X_train, y_train,epochs=epoch, batch_size=1, verbose=1)


        y_pred = model.predict(X_train)
        score = model.evaluate(X_train, y_train,verbose=2)
        print(score)

        model.save('temp/')

    except:
        messagebox.showerror('Error', "Parameters out of range.")
        return



def show(x, y, col_type):

    root = Tk()
    root.title('Deep Neural Network')

    Label(root, 
        text="A neural network is trained with the selected data and its accuracy shown."
        ).grid(row=0, column=0, columnspan=3)

    # x_train = tf.convert_to_tensor(x)
    # y_train = tf.convert_to_tensor(y)

    # print(y_train)

    # print(x)
    # print(y)

    Label(root, text="No. of layers (integer > 3, default = 3)").grid(row=1, column=0)

    layers = Entry(root)
    layers.insert(END, '3')
    layers.grid(row=2, column=0)

    Label(root, text="Epochs (integer > 1, default = 5)").grid(row=1, column=1)

    epoch = Entry(root)
    epoch.insert(END, '5')
    epoch.grid(row=2, column=1)

    Label(root, text="Test/train split (float 0 < 1, default = 0.1)").grid(row=1, column=2)

    split = Entry(root)
    split.insert(END, '0.1')
    split.grid(row=2, column=2)
    
    root.bind('<Return>', lambda:train(x, y, layers.get(), epoch.get(), split.get()))
    
    Button(root, text='Train Neural Network', command=lambda: train(x, y, layers.get(), epoch.get(), split.get())).grid(row=3, column=0, columnspan=3)




    # Label(root, 
    #     text="Neural Network score is "+str(score)
    #     ).pack()

    root.mainloop()


x, y, col_type = clean.up()
show(x, y, col_type)