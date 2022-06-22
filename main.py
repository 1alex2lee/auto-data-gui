from tkinter import *
from tkinter import filedialog, Scrollbar, messagebox
import pandas as pd
import graphs, thresholds, logreg, os, os.path, errno, clean, decisiontree

root = Tk()
root.title('Auto Data Analyser')



## OPEN FIL FRAME
open_file_f = LabelFrame(root, text='Select file', padx=5, pady=5)
open_file_f.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

columns = []

def select_file():
    global columns, select_file_l, path

    root.filename = filedialog.askopenfilename(initialdir='/Documents', 
        title='Select Excel File', filetypes = [('Excel files', '.xlsx .xls')])
    csv = pd.read_excel(root.filename)
    # path = os.path.join(sys.path[0], 'temp/data.csv')
    
    path = 'temp/'
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

    csv.to_csv('temp/data.csv')

    select_file_l = Label(open_file_f, text=str(root.filename)+' selected', padx=5, pady =5)
    select_file_l.grid(row=1, column=0)

    columns = []
    for c in csv.columns[0:]:
        columns.append(str(c))

    refresh_checkboxes()

select_file_b = Button(open_file_f, text='Select Excel File', command=select_file)
select_file_b.grid(row=0, column=0, padx=5, pady=5)

select_file_l = Label(open_file_f, text='No file selected', padx=5, pady =5)
select_file_l.grid(row=1, column=0)




## SELECT VARS AND RESULT FRAME
select_vars_f = LabelFrame(root, text='Select variables', padx=5, pady=5)
select_vars_f.grid(row=1, column=0, padx=5, pady=5)

select_rest_f = LabelFrame(root, text='Select result', padx=5, pady=5)
select_rest_f.grid(row=1, column=1, padx=5, pady=5)

selected_vars = {}
selected_rest = {}

def refresh_checkboxes():
    global selected_vars, selected_rest

    for widgets in select_vars_f.winfo_children():
        widgets.destroy()

    for widgets in select_rest_f.winfo_children():
        widgets.destroy()

    selected_vars = {}
    selected_rest = StringVar()

    for c in columns:
        selected_vars[c] = IntVar()

        var_checkbutton = Checkbutton(select_vars_f, text=c, variable=selected_vars[c], onvalue=1, offvalue=0)
        var_checkbutton.deselect()
        var_checkbutton.pack()

        res_checkbutton = Checkbutton(select_rest_f, text=c, variable=selected_rest, onvalue=c)
        res_checkbutton.deselect()
        res_checkbutton.pack()




## CONFIRM VARS AND RESULT FRAME
# confrim_f = LabelFrame(root, padx=5, pady=5)
# confrim_f.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# preview_l = Label(confrim_f, text='No variables and result selected', padx=5, pady=5)
# preview_l.grid(row=1, column=0, sticky=E)

# def preview():
#     global columns, selected_vars, selected_rest, preview_l

#     vars_empty = True
#     rest_empty = True

#     vars_preview = 'Varibles selected: '
#     rest_preview = 'Result selected: '

#     for c in columns:
#         if selected_vars[c].get() == 1:
#             vars_preview += str(c) + '; '
#             vars_empty = False
#         if selected_rest.get() == c:
#             rest_preview += str(c) + '.'
#             rest_empty = False

#     preview_l.destroy()

#     if vars_empty:
#         if rest_empty:
#             preview_l = Label(confrim_f, text='No variables and result selected', padx=5, pady=5)
#         else:
#             preview_l = Label(confrim_f, text='No variables selected.'+'\n'+rest_preview, padx=5, pady=5)
#     else:
#         if rest_empty:
#             preview_l = Label(confrim_f, text=vars_preview+'\n'+'No result selected.', padx=5, pady=5)
#         else:
#             preview_l = Label(confrim_f, text=vars_preview+'\n'+rest_preview, padx=5, pady=5)

#     preview_l.grid(row=1, column=0, sticky=W)

# confirm_b = Button(confrim_f, text='Confirm variables and result', command=preview)
# confirm_b.grid(row=0, column=0)




## NEXT STEPS FRAME
next_f = LabelFrame(root, padx=5, pady=5)
next_f.grid(row=1, column=2, rowspan=2, padx=5, pady=5)

def save():
    global columns, selected_vars, selected_rest, preview_l

    try:
        df_x = pd.read_csv('temp/data.csv', index_col=0)
    except:
        messagebox.showerror('Error', 'No file selected!')

    df_x = pd.DataFrame(df_x)
    df_y = df_x

    vars_empty = True
    rest_empty = True

    for c in columns:
        if selected_vars[c].get() != 1:
            df_x = df_x.drop(columns=c)
        else:
            vars_empty = False
        if selected_rest.get() != c:
            df_y = df_y.drop(columns=c)
        else:
            rest_empty = False

    if vars_empty:
        if rest_empty:
            messagebox.showerror('Error', 'No variables and result selected.')
            return False
        else:
            messagebox.showerror('Error', 'No variables selected.')
            return False
    else:
        if rest_empty:
            messagebox.showerror('Error', 'No result selected.')
            return False
        else:
            df_x.to_csv('temp/data_x.csv')
            df_y.to_csv('temp/data_y.csv')
            return True

def show_graphs():
    if save():
        x, y = clean.up()
        graphs.show(x , y)

next_b = Button(next_f, text='Show graphs', command=show_graphs)
next_b.grid(row=0, column=0)

def show_thresholds():
    if save():
        x, y = clean.up()
        thresholds.show(x, y)

next_b = Button(next_f, text='Show thresholds', command=show_thresholds)
next_b.grid(row=1, column=0)

def show_logreg():
    if save():
        x, y = clean.up()
        logreg.show(x, y)

next_b = Button(next_f, text='Show logreg', command=show_logreg)
next_b.grid(row=2, column=0)

def show_decisiontree():
    if save():
        x, y = clean.up()
        decisiontree.show(x, y)

next_b = Button(next_f, text='Show decision tree', command=show_decisiontree)
next_b.grid(row=3, column=0)


root.mainloop()