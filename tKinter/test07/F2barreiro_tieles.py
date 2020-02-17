from tkinter import *
from tkinter import ttk
from test07.F3barreiro_tieles import Simon


root = Tk()
f = ttk.Frame(root)
f.pack()
simon1 = Simon(f)
simon1.grid(column=0, row=0)
simon2 = Simon(f, width=600, height=600)
simon2.grid(column=0, row=1)
root.mainloop()
