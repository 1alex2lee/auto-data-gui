from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import frames

def show():

    root = Tk()
    root.title('Graphs')

    frame = frames.ScrollableFrame(root)

    Label(root, text="The below graph show each variable's relationship with the result.").pack()
    
    try:
        x = pd.read_csv('temp/data_x.csv', index_col=0)
        y = pd.read_csv('temp/data_y.csv', index_col=0)
    except:
        return

    for y_col in y.columns:
        figure = plt.Figure(figsize=(5,5), dpi=80)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, frame.scrollable_frame)
        chart_type.get_tk_widget().pack()
        ax.set_title('Variables againast '+y_col, fontsize=10)
        for x_col in x.columns:
            df = pd.DataFrame()
            df['x'] = x[x_col]
            df['y'] = y[y_col]
            df.sort_values('x', inplace=True)
            df.plot(x='x', y='y', ax=ax, label=x_col, xlabel='Variables', ylabel=y_col)
            ax.legend(loc='center right', fontsize=8)

    frame.pack()

    root.mainloop()

# show()