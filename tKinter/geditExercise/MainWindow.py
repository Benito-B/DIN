from geditExercise.GeditConfig import ConfigWindow
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def new_window(r) -> None:
    global new
    if new is None:
        new = ConfigWindow(Toplevel(r))
        root.iconify()


root = Tk()
menu = Menu()
new = None
ttk.Button(root, text="Modal dialog >inside<", command=lambda: filedialog.asksaveasfile()).pack()
menubar = Menu(root)
menu_edit = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=menu_edit, label='Edit')
menu_edit.add_command(label='Options', command=lambda: new_window(root))
root['menu'] = menubar
root.mainloop()
