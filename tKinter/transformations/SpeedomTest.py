from tkinter import *
from tkinter import ttk
from transformations.Speedodom import Speedodom

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

canvas = Speedodom(root, width=500, height=500)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

root.update()
root.mainloop()
