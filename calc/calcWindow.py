from tkinter import *
from tkinter import ttk


class CalcWindow(object):

    zero_division = "ZERO DIVISION ERROR"

    def __init__(self):
        self.window = Tk()
        self.window.geometry("240x150")
        self.window.resizable(False, False)
        self.hasDot = False
        self.op1 = ""
        self.operation = ""
        self.op2 = ""
        self.memory = ""
        self.justoperated = False
        self.pantalla = StringVar()
        # "Screen"
        Label(self.window, textvariable=self.pantalla, border=1, relief=GROOVE, width=24).pack()
        self.mainframe = ttk.Frame(self.window, padding="5 5 5 5")
        self.mainframe.pack()
        self.window.title("Calculadora")
        self.setbuttons(self.pantalla)
        self.window.mainloop()

    def setbuttons(self, p: StringVar):
        # Buttons for numbers
        for r in range(3):
            for c in range(1, 4):
                text = str(10 - (r * 3 + c))
                self.addbutton(self.mainframe, text, c, r)
        self.addbutton(self.mainframe, "0", 3, 3)
        # Button for the dot
        Button(self.mainframe, width=2, text=".", command=lambda: self.managedot(p))\
            .grid(column=1, row=3, sticky=W)
        # Buttons for operations
        Button(self.mainframe, width=2, text="=", command=lambda: self.operate(p, self.operation))\
            .grid(column=2, row=3, sticky=W)
        Button(self.mainframe, width=2, text="/", command=lambda: self.getoperator(p, "/"))\
            .grid(column=4, row=0, sticky=W)
        Button(self.mainframe, width=2, text="*", command=lambda: self.getoperator(p, "*"))\
            .grid(column=4, row=1, sticky=W)
        Button(self.mainframe, width=2, text="-", command=lambda: self.getoperator(p, "-"))\
            .grid(column=4, row=2, sticky=W)
        Button(self.mainframe, width=2, text="+", command=lambda: self.getoperator(p, "+"))\
            .grid(column=4, row=3, sticky=W)
        # Buttons for memory and cleaning the screen
        Button(self.mainframe, width=2, text="Mc", command=lambda: self.memoryclear())\
            .grid(column=5, row=0, sticky=W)
        Button(self.mainframe, width=2, text="Ms", command=lambda: self.memoryset(p))\
            .grid(column=5, row=1, sticky=W)
        Button(self.mainframe, width=2, text="Mr", command=lambda: self.memoryrecover(p))\
            .grid(column=5, row=2, sticky=W)
        Button(self.mainframe, width=2, text="Del", command=lambda: self.clear()).grid(column=5, row=3, sticky=W)

    def addbutton(self, f: Frame, symbol: str, col: int, row: int):
        buttonoptions = dict()
        buttonoptions["width"] = 2
        buttonoptions["text"] = symbol
        buttonoptions["command"] = lambda: self.add(self.pantalla, symbol)
        Button(f, buttonoptions).grid(column=col, row=row, sticky=W)

    def clear(self):
        self.pantalla.set("")
        self.op1 = ""
        self.op2 = ""
        self.operation = ""

    def operate(self, screen: StringVar, operator: str):
        if screen.get() == self.zero_division:
            self.clear()
            return
        if self.op1 == "":
            return
        self.op2 = screen.get()
        if operator == "+":
            screen.set(float(self.op1) + float(self.op2))
        elif operator == "-":
            screen.set(float(self.op1) - float(self.op2))
        elif operator == "*":
            screen.set(float(self.op1) * float(self.op2))
        elif operator == "/":
            if float(self.op2) == float(0):
                screen.set(self.zero_division)
            else:
                screen.set(float(self.op1) / float(self.op2))
        # Reset the variables to get ready for the next operation
        self.op1 = ""
        self.operation = ""
        self.justoperated = True

    def getoperator(self, screen: StringVar, op: str):
        if screen.get() == self.zero_division:
            return
        if self.op1 == "":
            self.op1 = screen.get()
            screen.set("")
        self.operation = op

    def add(self, r: StringVar, x: str):
        if self.justoperated:
            r.set("")
            self.justoperated = False
        current = r.get()
        if r.get() == "0" and x == "0" and not self.hasDot:
            return
        current += x
        r.set(current)

    def managedot(self, r: StringVar):
        if not self.hasDot:
            r.set(r.get() + '.')
            self.hasDot = True
        else:
            if r.get()[-1] == ".":
                r.set(r.get()[:-1])
                self.hasDot = False

    def memoryset(self, r: StringVar):
        self.memory = r.get()
        r.set("")

    def memoryclear(self):
        self.memory = ""

    def memoryrecover(self, r: StringVar):
        r.set(self.memory)


if __name__ == "__main__":
    w = CalcWindow()
