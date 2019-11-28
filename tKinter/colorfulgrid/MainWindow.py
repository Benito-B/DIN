from tkinter import *
from tkinter import ttk


def chcolor(cb: ttk.Combobox, v_checks: list, h_checks: list, labs: list, color: StringVar) -> None:
    """
    Changes the color of the selected marks to the one in the combobox
    :param cb: the combobox
    :param v_checks: vertical checkboxes
    :param h_checks: horizontal checkboxes
    :param labs: list of lists with the labels
    :param color: the color StringVar
    :return: none
    """
    cb.select_clear()
    for x in range(len(labs)):
        for y in range(len(labs[x])):
            if v_checks[x].get() and h_checks[y].get():
                labs[x][y].config(background=color.get())


def clearcolor(labs: list) -> None:
    """
    Clears the colors on the labels
    :param labs: list of lists with the labels
    :return: None
    """
    for l in labs:
        for elem in l:
            elem['background'] = ''


# FRAMEWORK
window = Tk()
# window.rowconfigure(0, weight=1, minsize=20)
# window.columnconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
# Creating the frame for the grid
frame = ttk.Frame(window)
frame.grid(column=0, row=0, sticky="NSWE")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
# Dictionary for storing the label references
labels = list()
# Variables for the checks
v_check_vars = list()
h_check_vars = list()
# Variable for the colors combobox
color_var = StringVar()
# Horizontal checkbuttons
for i in range(4):
    h_check_vars.append(BooleanVar())
    ttk.Checkbutton(frame, variable=h_check_vars[i]).grid(row=0, column=i + 1)
# Vertical checkbuttons
for i in range(4):
    v_check_vars.append(BooleanVar())
    ttk.Checkbutton(frame, variable=v_check_vars[i]).grid(row=i + 1, column=0)
# Adding the labels to the grid
for r in range(4):
    labels.append([])
    for c in range(4):
        lab = ttk.Label(frame, text=r + c, relief='groove')
        lab.grid(row=r + 1, column=c + 1, sticky="NSWE")
        labels[r].append(lab)
# Clear button
clear_bt = ttk.Button(frame, width=3, text='CLR', command=lambda: clearcolor(labels))
clear_bt.grid(row=0, column=0)
# set Button
set_bt = ttk.Button(frame, width=3, text='Set', command=lambda: chcolor(combo, v_check_vars, h_check_vars,
                                                                        labels, color_var))
set_bt.grid(row=5, column=0)
# Color combobox
combo_values = ('red', 'blue', 'black', 'yellow')
combo = ttk.Combobox(frame, textvar=color_var, state='readonly')
combo['values'] = combo_values
combo.grid(columnspan=4, row=5, column=1, padx=5, sticky="NSWE")
combo.bind("<<ComboboxSelected>>", lambda e: chcolor(combo, v_check_vars, h_check_vars, labels, color_var))
combo.current(1)
# Specify the sizes of the first row and column
frame.grid_rowconfigure(0, minsize=30, weight=0)
frame.grid_columnconfigure(0, minsize=20, weight=0)
# loops for specifying the size of the rest of the rows and columns
col_count, row_count = frame.grid_size()
for col in range(1, col_count):
    frame.grid_columnconfigure(col, minsize=50, weight=1)
for row in range(1, row_count - 1):  # -1 so it ignores the last one
    frame.grid_rowconfigure(row, minsize=100, weight=1)
# Specify the size of the last row
frame.grid_rowconfigure(5, minsize=20, weight=0)
# Refresh screen and launch it
window.update()
window.minsize(window.winfo_width(), window.winfo_height())
window.mainloop()
