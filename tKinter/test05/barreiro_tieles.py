from random import randint
from tkinter import *
from tkinter import ttk


def putMine(prob):
    if randint(1, prob) == 1:
        return 1
    else:
        return 0


def isvalid(r: int, c: int) -> bool:
    """
    Returns true if the coords are within range, false otherwise
    :r: row to check
    :c: column to check
    :return: bool indicating if the coordinates are valid
    """
    if r < 0 or r > 9 or c < 0 or c > 9:
        return False
    return True


def count_mines(w: ttk.Widget, r: int, c: int) -> None:
    """
    :w: Widget where I need to display the number of mines
    :r: Row where it is located in the list
    :c: Column where it is located in the list
    :return: None
    """
    # print("DEBUG r/c -> ", r, c)
    global intvars
    mines = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            print(x, y)
            if isvalid(c+x, r+y):
                print("intvar:", intvars[c+x][r+y].get())
                if intvars[c+x][r+y].get() == 1:
                    mines += 1
    w['text'] = mines


def init():
    """
    Method that builds the labels and intvars needed for it. It is also called when pressing the New Game button
    """
    # Variables for initializing the game
    DIFFICULTY = 10
    global labels
    global intvars
    global readylabel
    labels = list()
    intvars = list()
    readylabel.set("Ready to play!")
    # Loop for adding the labels
    for r in range(10):
        intvars.append([])
        labels.append([])
        for c in range(10):
            intvars[r].append(IntVar())
            intvars[r][c].set(putMine(DIFFICULTY))
            labels[r].append(ttk.Label(frame, text=" ", relief=RAISED, anchor="center"))
            labels[r][c].grid(row=r, column=c, sticky="NSWE")
            bind_label(labels[r][c], r, c)


def bind_label(w: ttk.Widget, r: int, c: int) -> None:
    """
    Binds the label with the events needed to display the ammount of bombs next to it
    :w: Widget to bind
    :r: Row where the widget is located in the list
    :c: Column where the widget is located in the list
    :return: None
    """
    print("Binded label: ", r, c)
    w.bind('<Enter>', lambda e: count_mines(w, r, c))
    w.bind('<Leave>', lambda e: delete_text(w))
    w.bind('<Button-1>', lambda e: check_mine(w, r, c))


def check_mine(w: ttk.Widget, r: int, c: int) -> None:
    """
    Checks if the given mine contains a bomb or not and changes it's color based on it
    :w: Label to check
    :r: row where the intvar is located in the list
    :c: column where the intvar is located in the list
    :return: none
    """
    global intvars
    global readylabel
    if intvars[r][c].get() == 1:
        w['background'] = 'red'
        readylabel.set("YOU LOOSER!!")
    else:
        w['background'] = 'cyan'


def delete_text(w: ttk.Widget) -> None:
    """
    Deletes the text of the given Widget
    :w: Widget which's text is going to be deleted
    :return: None
    """
    w['text'] = ''


# FRAMEWORK
window = Tk()
window.title('Minesweeper')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
# Creating the frame for the grid
frame = ttk.Frame(window, padding=8, relief=RAISED)
frame.grid(column=0, row=0, sticky=N)
# Lists for holding the IntVars and labels
labels = None
intvars = None
# Variable for the ready to play label
readylabel = StringVar()
# Call the init method to build the frame
init()
# Adding the label and button on the last row
ttk.Label(frame, textvariable=readylabel, relief=RAISED, anchor="center")\
    .grid(row=10, column=0, columnspan=5, sticky="NSWE")
Button(frame, text="New Game", relief=RAISED, command=init)\
    .grid(row=10, column=5, columnspan=5, sticky="NSWE")
# Loop for setting the size and weights
col_count, row_count = frame.grid_size()
for col in range(col_count):
    frame.grid_columnconfigure(col, minsize=30, weight=0)
for row in range(row_count):
    frame.grid_rowconfigure(row, minsize=30, weight=0)
# Refresh screen and launch it
window.update()
window.minsize(window.winfo_width(), window.winfo_height())
window.mainloop()
