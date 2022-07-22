from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import clean, threading, keras

# mnist = tf.keras.datasets.mnist

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0



def predict(x):

    predict_window = Tk()
    predict_window.title('Predict Using Neural Network Model')

    model = keras.models.load_model('temp/')

    def predict_y(event=None):
        x_pred = []
        for c in range (cols_no):
            print('{} is {}'.format(x_cols[c], x_cols_entry[c].get()))
            x_pred.append(float(x_cols_entry[c].get()))
        
        Label(predict_window, text='Predicted y value is {}'.format(model.predict(x_pred))).grid(row=cols_no+2, column=0, columnspan=2, padx=5, pady=5)

    # print(x.columns[0])

    x_cols = x.columns
    cols_no = len(x_cols)
    x_cols_entry = []

    for c in range (cols_no):
        Label(predict_window, text=x_cols[c]).grid(row=c, column=0, padx=5, pady=5)
        x_cols_entry.append(Entry(predict_window))
        x_cols_entry[c].grid(row=c, column=1, padx=5, pady=5)

    Button(predict_window, text='Predict', command=predict_y).grid(row=cols_no+1, column=0, columnspan=2, padx=5, pady=5)
    predict_window.bind('<Return>', predict_y)

    predict_window.mainloop()




def model(x, y, layers, epoch, split):

    done = False

    class CustomCallback(keras.callbacks.Callback):

        def on_epoch_end(self, epoch, logs=None):
            global current_step, total_steps
            current_step += 1
            pb['value'] = 100*current_step/total_steps
            # print(pb['value'])

        def on_test_end(self, logs=None):
            global current_step, total_steps
            current_step += 1
            pb['value'] = 100*current_step/total_steps
            # print(pb['value'])

        def on_predict_end(self, logs=None):
            global current_step, total_steps
            current_step += 1
            pb['value'] = 100*current_step/total_steps
            # print(pb['value'])

        def on_train_batch_end(self, batch, logs=None):
            global current_step, total_steps
            current_step += 1
            pb['value'] = 100*current_step/total_steps
            # print(pb['value'])




    def inputs_ok(layers, epoch, split):
        try: 
            layers = int(layers)
        except:
            messagebox.showerror('Error', "No. of layers is not an integer.")
            return False
        try: 
            epoch = int(epoch)
        except:
            messagebox.showerror('Error', "Epochs is not an integer.")
            return False
        try: 
            split = float(split)
        except:
            messagebox.showerror('Error', "Split is not a decimal.")
            return False
        if layers < 3:
            messagebox.showerror('Error', "No. of layers is too small.")
            return False
        if epoch < 1:
            messagebox.showerror('Error', "Epochs is too small.")
            return False
        if split >= 1:
            messagebox.showerror('Error', "Split is too big.")
            return False
        if split <= 0:
            messagebox.showerror('Error', "Split is too small.")
            return False
        else:
            return True


    


    def train(x, y, layers, epoch, split, event=None):

        global total_steps, current_step

        pb.start()

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=split, random_state=42)
                
        scaler = StandardScaler().fit(X_train)
        X_train = scaler.transform(X_train)
        # X_test = scaler.transform(X_test)

        # print(X_train.shape)

        model = Sequential()
        model.add(Dense(8, activation='relu', input_shape=(X_train.shape[1],)))

        current_step = 0
        total_steps = epoch*X_train.shape[0] + epoch + 2
        done = False

        for l in range (layers-2):
            model.add(Dense(8, activation='relu'))

        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy',
        optimizer='sgd',
        metrics=['accuracy'])

        model.fit(X_train, y_train,epochs=epoch, batch_size=1, verbose=1, callbacks=[CustomCallback()])

        y_pred = model.predict(X_train, callbacks=[CustomCallback()])
        score = model.evaluate(X_train, y_train, verbose=1, callbacks=[CustomCallback()])
        print(score)

        model.save('temp/')

        done = True
        print('done is '+str(done))
        print('current at {} of {} steps'.format(current_step, total_steps))

        pb.stop()
        train_window.quit()
        # train_window.destroy()

        predict(x)

        # return True




    if inputs_ok(layers, epoch, split):

        # try:

        train_window = Tk()
        # root.geometry('300x120')
        train_window.title('Training Neural Network Model')

        pb = ttk.Progressbar(
            train_window,
            orient='horizontal',
            mode='determinate',
            length=380
        )

        def cancel():
            # global done
            # done = True
            # pb['value']=100
            # t.join()
            train_window.destroy()
            
        Button(train_window, text='Cancel', command=cancel).grid(row=1, column=0, padx=5, pady=5)

        pb.grid(column=0, row=0, padx=10, pady=20)
        pb.start()

        layers = int(layers)
        epoch = int(epoch)
        split = float(split)

        t = threading.Thread(target=train, args=(x, y, layers, epoch, split))

        # def check_done():
        #     # global done
        #     if done:
        #         pb.stop()
        #         root.destroy()
        #     else:
        #         root.after(1, check_done)

        # check_done()

        t.start()


        # executor = concurrent.futures.ThreadPoolExecutor()
        # future = executor.submit(train, x, y, layers, epoch, split)
        # result = future.result()
        # while result:
        #     pb.stop()
        #     root.destroy()


        # root.wait_variable(done)

        # t.join()
        # print('the progress bar is at {}'.format(pb['value']))
        train_window.mainloop()


        # except:
        #     messagebox.showerror('Error', "Parameters out of range.")
        #     return

    # else:
    #     messagebox.showerror('Error', "Input error.")
    #     return


def show(x, y, col_type):

    show_window = Tk()
    show_window.title('Deep Neural Network')

    Label(show_window, 
        text="A neural network is trained with the selected data and its accuracy shown."
        ).grid(row=0, column=0, columnspan=3)

    # x_train = tf.convert_to_tensor(x)
    # y_train = tf.convert_to_tensor(y)

    # print(y_train)

    # print(x)
    # print(y)

    Label(show_window, text="No. of layers (integer >= 3, default = 3)").grid(row=1, column=0)

    layers = Entry(show_window)
    layers.insert(END, '3')
    layers.grid(row=2, column=0)

    Label(show_window, text="Epochs (integer > 1, default = 5)").grid(row=1, column=1)

    epoch = Entry(show_window)
    epoch.insert(END, '5')
    epoch.grid(row=2, column=1)

    Label(show_window, text="Test/train split (float 0 < 1, default = 0.01)").grid(row=1, column=2)

    split = Entry(show_window)
    split.insert(END, '0.01')
    split.grid(row=2, column=2)
    
    show_window.bind('<Return>', lambda event, l=layers.get(), e=epoch.get(), s=split.get(): model(x, y, l, e, s))
    
    Button(show_window, text='Train Neural Network', command=lambda:model(x, y, layers.get(), epoch.get(), split.get())).grid(row=3, column=0, columnspan=3)




    # Label(root, 
    #     text="Neural Network score is "+str(score)
    #     ).pack()

    show_window.mainloop()


x, y, col_type = clean.up()
show(x, y, col_type)
# model(x, y, 3, 5, 0.01)
# predict(x)