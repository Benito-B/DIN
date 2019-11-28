from tkinter import *
from tkinter.font import Font


class Mixer(object):

    def __init__(self, parent: Tk):
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        # Put the labels and intvars into tuples so I can easily access them later in the loop
        self.colors = (IntVar(), IntVar(), IntVar())
        self.colors[0].set(255)
        self.colors[1].set(255)
        self.colors[2].set(255)
        self.colorlabels = (Label(self.frame), Label(self.frame), Label(self.frame))
        self.button = None
        self.addelements()
        self.font = None


    def addelements(self) -> None:
        """
        Method to create the view and asign the intvars to the corresponding widgets
        """
        self.font = Font(family="Helvetica", size=16)
        # Red label
        Label(self.frame, width=5, height=3, font=self.font, text='Red').grid(column=0, row=0, sticky=W)
        # Loop for adding the buttons and labels
        for r in range(3):
            print(r)
            self.makebutton(self.frame, '-', 1, r)
            self.colorlabels[r].config(width=10, height=3, font=self.font, relief="solid", textvar=self.colors[r])
            self.colorlabels[r].grid(column=2, row=r, sticky=W)
            self.recolor(r)
            self.makebutton(self.frame, '+', 3, r)
        # Green label
        Label(self.frame, width=5, height=3, font=self.font, text='Green')\
            .grid(column=0, row=1, sticky=W)
        # Blue label
        Label(self.frame, width=5, height=3, font=self.font, text='Green') \
            .grid(column=0, row=2, sticky=W)
        # Mix Button
        self.button = Button(self.frame, text='Mix', font=self.font, width=10,
                             height=10, command=self.changebuttoncolor)
        self.button.grid(column=4, row=0, rowspan=3, sticky=W)

    def changebuttoncolor(self) -> None:
        """
        Changes the background color of the mix button
        :return: None
        """
        r = self.colors[0].get()
        g = self.colors[1].get()
        b = self.colors[2].get()
        self.button.config(bg=self.composecolor(r, g, b))

    def makebutton(self, f: Frame, symbol: str, col: int, row: int) -> None:
        """
        Makes a button and places it into the right position
        :param f: frame where the button will be added
        :param symbol: text on the button and used for lambda
        :param col: column where it should be placed
        :param row: row where it should be placed
        """
        buttonoptions = dict()
        buttonoptions["width"] = 2
        buttonoptions["text"] = symbol
        buttonoptions["font"] = self.font
        buttonoptions["relief"] = RAISED
        buttonoptions["command"] = lambda: self.changecolor(symbol, row)
        Button(f, buttonoptions).grid(column=col, row=row, sticky=W)

    def changecolor(self, symbol: str, r: int) -> None:
        """
        Changes the value of the intvar in the label and also triggers the recolor method
        :param symbol: plus or minus, identifies the operation
        :param r: row of the button, used to access the widgets in the tuples
        :return: None
        """
        if symbol == '+':
            if self.colors[r].get() + 5 > 255:
                return
            self.colors[r].set(self.colors[r].get() + 5)
        else:
            if self.colors[r].get() - 5 < 0:
                return
            self.colors[r].set(self.colors[r].get() - 5)
        self.recolor(r)

    def recolor(self, r: int) -> None:
        """
        Changes the background color of the corresponding label
        :param r: the index of the label for the tuple
        :return:
        """
        if r == 0:
            self.colorlabels[0].config(bg=self.composecolor(self.colors[0].get(), 0, 0))
        elif r == 1:
            self.colorlabels[1].config(bg=self.composecolor(0, self.colors[1].get(), 0))
        elif r == 2:
            self.colorlabels[2].config(bg=self.composecolor(0, 0, self.colors[2].get()))

    def start(self) -> None:
        """
        Starts the application
        :return: None
        """
        self.parent.mainloop()

    def composecolor(self, r: int, g: int, b: int) -> str:
        """
        Returns the RGB color composed with the indicated parameters
        :param r: red component
        :param g: green component
        :param b: blue component
        :return: hexadecimal representation of the color (#RRGGBB)
        """
        return '#' \
               + (str(hex(r))[2:]).upper().zfill(2) \
               + (str(hex(g))[2:]).upper().zfill(2) \
               + (str(hex(b))[2:]).upper().zfill(2)


if __name__ == "__main__":
    window = Tk()
    app = Mixer(window)
    app.start()