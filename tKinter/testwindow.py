from tkinter import *
from tkinter import messagebox

# Controller
def click(c: IntVar, x: int):
    c.set(c.get() + x)


if __name__ == "__main__":
    window = Tk()
    counter = IntVar()
    def showmessage():
        messagebox.showinfo('Veo que quieres salir...')
    # Model
    counter.set(0)
    # View
    frame = Frame(window)
    frame.pack()
    button = Button(frame, text='Sube', command=lambda: click(counter, 1))
    button.pack()
    button = Button(frame, text='Baja', command=lambda: click(counter, -1))
    button.pack()
    label = Label(frame, textvariable=counter)
    label.pack()
    # SO IT BEGINS
    window.protocol('WM_DELETE_WINDOW', showmessage)
    window.mainloop()
