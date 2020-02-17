from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, master): # Constructor
        self.master=master
        self.counter=0
        # build GUI
        self.label = ttk.Label(text="Press <space>", width=40)
        self.label.grid(row=1, column=1, sticky='w')

        # bind keys to buttons
        master.bind('<Key-space>', self.keyPressed)


    def ignore(self, event):
        print("ignore")
        return "break"

    def keyPressed(self, event):
        self.master.bind('<Key-space>', self.ignore)
        #self.master.unbind('<Key-space>')
        print("Step 1")
        self.counter = self.counter + 1
        self.label["text"] = str(self.counter)
        self.master.after(3000, self.bindit)
        print("Step  2")

    def bindit(self):
        self.master.bind('<Key-space>', self.keyPressed)
        print("Step 3 = ready for more input")


root = Tk()
root.option_add('*font', ('Arial', 11, 'bold'))
# root.attributes("-toolwindow", 1)

posX = root.winfo_screenwidth() - 500
posY = 30
root.geometry("+%d+%d" % (posX, posY))

root.title("Bind tester")
display = App(root)
root.mainloop()
