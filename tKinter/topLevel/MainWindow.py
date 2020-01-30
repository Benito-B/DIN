from tkinter import *
from tkinter import ttk


def new_window():
    new = Toplevel(root)
    var = StringVar()
    padded_frame = ttk.Frame(new, padding=15)
    padded_frame.pack()
    lf = ttk.LabelFrame(padded_frame, text="Themes", padding=10)
    lf.pack()
    s = ttk.Style()
    for t in s.theme_names():
        ttk.Radiobutton(lf, text=t, variable=var, value=t).pack()
    var.set(s.theme_use())
    new.update()
    new.minsize(new.winfo_width(), new.winfo_height())


root = Tk()
ttk.Button(root, text='New window', command=new_window).pack()
root.geometry("300x200+800+300")
root.mainloop()
