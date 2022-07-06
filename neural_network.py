from tkinter import *
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


def show(x, y, col_type):

    root = Tk()
    root.title('Thresholds')

    Label(root, 
        text="A neural network is trained with the selected data and its accuracy shown."
        ).pack()

    # x_train = tf.convert_to_tensor(x)
    # y_train = tf.convert_to_tensor(y)

    # print(y_train)

    print(x)
    print(y)


    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    
    scaler = StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)


    model = Sequential()
    model.add(Dense(8, activation='relu', input_shape=(1,)))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',
    optimizer='sgd',
    metrics=['accuracy'])
    model.fit(X_train, y_train,epochs=8, batch_size=1, verbose=1)


    y_pred = model.predict(X_test)
    score = model.evaluate(X_test, y_test,verbose=1)
    print(score)




    Label(root, 
        text=""
        ).pack()

    # root.mainloop()


x, y, col_type = clean.up()
show(x, y, col_type)