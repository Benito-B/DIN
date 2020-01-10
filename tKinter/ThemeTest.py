from tkinter import *
from tkinter import ttk


root = Tk()
root.rowconfigure(0, weight=1, minsize=20)
root.columnconfigure(0, weight=1)
pane = ttk.Frame(root)
pane.pack()
current_theme = StringVar()
s = ttk.Style()
s.configure('MyButton.TButton', font='helvetica 30', foreground='red', padding=30, anchor='right')
s.configure('.', background='black')  # Turns everything black
s.map('.',
      background=[('disabled', 'black'), ('active', 'yellow')],
      relief=[('active', '!disabled', 'sunken')])
label = ttk.Label(pane, text="I'm a label")
label.pack()
button = ttk.Button(pane, text="I'm a strange Button", style='MyButton.TButton')
button.pack()
label.bind('<1>', lambda e: print(button['style']))
radio = ttk.Radiobutton(pane, text="I'm a RadioButton")
radio.pack()
checkbox = ttk.Checkbutton(pane, text="I'm a CheckButton")
checkbox.pack()
combo = ttk.Combobox(pane, values=s.theme_names(), textvar=current_theme)
combo.pack()
combo.set(s.theme_use())
combo.bind('<<ComboboxSelected>>', lambda e: s.theme_use(current_theme.get()))
s.configure('TButton', font='helvetica 48')
root.mainloop()
