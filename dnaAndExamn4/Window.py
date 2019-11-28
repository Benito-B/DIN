from tkinter import *
from tkinter.font import Font


class DNACounter(object):

    def __init__(self, parent: Tk):
        self.parent = parent
        self.data = StringVar()
        self.resultdata = StringVar()
        self.frame = Frame(parent)
        self.frame.pack()
        self.addelements()
        self.font = None

    def start(self):
        self.parent.mainloop()

    def addelements(self):
        self.font = Font(family="Helvetica", size=16, weight="bold")
        text = Text(self.frame, width=25, height=5, font=self.font)
        text.pack()
        Button(self.frame, text='Calculate the DNA and 4th examn sequence',
               command=lambda: self.calculatedna(text.get("1.0", "end-1c"),
                                                 self.resultdata)).pack()
        Label(self.frame, textvar=self.resultdata).pack()
        menubar = Menu(self.parent)
        lettersmenu = Menu(menubar)
        lettersmenu.add_command(label='Delete As', command=lambda: self.deletefromdna('A', text))
        lettersmenu.add_command(label='Delete Ts', command=lambda: self.deletefromdna('T', text))
        lettersmenu.add_command(label='Delete Cs', command=lambda: self.deletefromdna('C', text))
        lettersmenu.add_command(label='Delete Gs', command=lambda: self.deletefromdna('G', text))
        menubar.add_cascade(label='File', menu=lettersmenu)
        menubar.add_command(label='Quit', command=lambda: quit(self.parent))
        self.parent.config(menu=menubar)

    def deletefromdna(self, letter: str, text: Text) -> None:
        currentdna = text.get("1.0", "end-1c").upper()
        currentdna = currentdna.split(letter)
        currentdna = ''.join(currentdna)
        text.delete("1.0", "end")
        text.insert("1.0", currentdna)
        self.calculatedna(currentdna, self.resultdata)
        self.font = Font(family="Helvetica", size=16, weight="normal", slant="italic")
        text.config(font=self.font)

    def calculatedna(self, data: str, resultdata: StringVar) -> None:
        result = "  The DNA and 4th examn chain contains-> "
        letters = dict()
        letters['A'] = 0
        letters['T'] = 0
        letters['C'] = 0
        letters['G'] = 0
        for letter in letters.keys():
            letters[letter] = data.upper().count(letter)
            result += "{0}s: {1}  ".format(letter, letters[letter])
        resultdata.set(result)


if __name__ == "__main__":
    window = Tk()
    app = DNACounter(window)
    app.start()
