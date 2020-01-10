from tkinter import *
from tkinter import ttk
from tkinter import colorchooser, messagebox


def changecolor():
    global label
    color = colorchooser.askcolor(initialcolor='#FF6688')
    if color[1] is not None:
        if messagebox.askyesno(message='Estás seguro de que ese color es el que quieres?', icon='question',
                               title='Confirmar?'):
            label['background'] = color[1]


root = Tk()
root.rowconfigure(0, weight=1, minsize=20)
root.columnconfigure(0, weight=1)
label = ttk.Label(root, text="I'm a label!", anchor="center")
label.grid(row=0, column=0, sticky="NSWE")
ttk.Button(root, text="Change the label background color", command=changecolor).grid(row=1, column=0)
root.mainloop()
