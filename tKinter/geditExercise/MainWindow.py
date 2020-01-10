from geditExercise.GeditConfig import ConfigWindow
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
menu = Menu()
ttk.Button(root, text="Modal dialog >inside<", command=lambda: filedialog.asksaveasfile()).pack()
menubar = Menu(root)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_edit, label='Edit')
menu_edit.add_command(label='Options', command=lambda: ConfigWindow().start())
root['menu'] = menubar
root.mainloop()
