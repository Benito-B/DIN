import random
import threading
import time
from tkinter import *
from tkinter import ttk


def force_wait():
    var.set(0)
    for i in range(247):
        time.sleep(random.randrange(1, 15) / 10)
        var.set(var.get() + 10)


def increase_bar():
    threading.Thread(target=force_wait).start()


root = Tk()
root.rowconfigure(0, weight=1, minsize=20)
root.columnconfigure(0, weight=1)
# Creating the frame for the grid
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky="NSWE")
var = IntVar()
var.set(0)
p = ttk.Progressbar(frame, orient=HORIZONTAL, length=200, mode='determinate', variable=var, maximum=247)
p.grid(row=0, column=0)
ttk.Button(text='Turn it on', command=increase_bar).grid(row=1, column=0)
root.geometry("300x200-10-20")
root.mainloop()
