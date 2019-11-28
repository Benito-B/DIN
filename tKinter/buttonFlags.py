from tkinter import *
from tkinter import ttk

window = Tk()
var = StringVar()
ftw = StringVar()
radiovar = StringVar()
combovar = StringVar()
var.set("Menea el ratón sobre el botón y pulsa intro")
window.minsize(300, 150)
TOGGLE_BUTTON = 'ToggleButton.TButton'
style = ttk.Style()
sunk = False


def sunkit(*args) -> None:
    global sunk
    if sunk:
        style.configure(TOGGLE_BUTTON, relief=SUNKEN)
    else:
        style.configure(TOGGLE_BUTTON, relief=RAISED)
    sunk = not sunk


def wtfit(*args) -> None:
    print("Check state:", check.state())


Label(window).grid(row=0, column=0)
Label(window).grid(row=0, column=0)
bt = ttk.Button(window, text="Soy un botón", style=TOGGLE_BUTTON)
bt.bind('<1>', lambda e: var.set(bt.state()))
bt.bind('<Double-3>', sunkit)
bt.grid(row=1, column=0)
check = ttk.Checkbutton(window, text='FTW', command=lambda: window.title(ftw.get()), variable=ftw,
                        onvalue='FTW!!!', offvalue='WTF???')
check.grid(row=1, column=1)
check.bind('<3>', wtfit)
Label(window, textvar=var).grid(row=1, column=2)
rbt = ttk.Radiobutton(window, text='Tentacool', variable=radiovar, value='Tentacruel')
rbt.grid(row=2, column=0)
ttk.Radiobutton(window, text='Pikachu', variable=radiovar, value='PeekAtChu').grid(row=2, column=1)
ttk.Radiobutton(window, text='Arcanine', variable=radiovar, value='Arcanein').grid(row=2, column=2)
ttk.Label(window, text='Your pokemon evolution is: ').grid(row=3, column=0, columnspan=2)
ttk.Label(window, textvar=radiovar).grid(row=3, column=2)
combo_values = ('Uno', 'Dos', 'Tres', 'Cuatro')
combo = ttk.Combobox(window, textvar=combovar, state='readonly')
combo['values'] = combo_values
combo.set('Elige uno')
combo.grid(row=4, column=0)
combo.bind("<<ComboboxSelected>>", lambda e: combo.select_clear())
ttk.Label(window, text='Seleccionado:').grid(row=4, column=1)
ttk.Label(window, textvar=combovar).grid(row=4, column=2)
ttk.Button(window, text='Mark something', command=lambda: check.invoke())\
    .grid(row=5, column=0, columnspan=3, sticky="EW")
window.bind('<Return>', lambda e: var.set(rbt.state()))
window.mainloop()
