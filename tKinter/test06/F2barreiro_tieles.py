from tkinter import *
from tkinter import ttk


class F2window:

    def __init__(self, t: Toplevel = None):
        """
        Builds the new item and sets the default values of the window itself
        @param t: Toplevel, if given converts the window into a toplevel window of another one, if not, builds a Tk()
        """
        self.tk = None
        if t is None:
            self.tk = Tk()
        else:
            self.tk = t
        self.tk.title("Preferences")
        # self.tk.geometry("240x240")
        self.root = None
        self.notebook = None
        self.labeled_frame = None
        self.paned_frame = None
        self.fill()

    def fill(self) -> None:
        """
        This method builds the main window's widgets and assigns them their values
        """
        self.root = ttk.Frame(self.tk, padding=0)
        self.root.grid(column=0, row=0, sticky="NSWE")
        self.notebook = ttk.Notebook(self.root, padding=0)
        self.labeled_frame = ttk.Frame(self.notebook, padding=10, relief=SUNKEN)
        self.fill_labeled_frame()
        self.labeled_frame.grid(column=0, row=0, sticky="NSWE")
        self.paned_frame = ttk.Frame(self.notebook, padding=10, relief=SUNKEN)
        self.fill_paned_frame()
        self.paned_frame.grid(column=0, row=1, sticky="NSWE")
        self.notebook.add(self.labeled_frame, text="Label Frames")
        self.notebook.add(self.paned_frame, text="Paned Windows")
        self.notebook.grid(column=0, row=0, sticky="NSWE")
        self.add_radios()

    def fill_labeled_frame(self) -> None:
        """
        Fills the labeled frame with it's corresponding content
        """
        labels = [["LF A", "LF B"], ["LF C", "LF D"]]
        for x in (0, 1):
            for y in (0, 1):
                frame = ttk.Labelframe(self.labeled_frame, height=120, width=120, text=labels[x][y],
                                       labelanchor=NW if y < 1 and x < 1 else NE if y < 1 else SW if x < 1 else SE)
                # I know that using ternary operators for that makes it harder to read, but it fits in just one line!
                frame.grid(column=x, row=y, sticky="NSWE")
                frame.configure(underline=3)

    def fill_paned_frame(self) -> None:
        """
        Fills the paned frame with it's corresponding content
        """
        self.paned_frame.configure(padding=(30, 20))
        p = ttk.PanedWindow(self.paned_frame, orient=VERTICAL)
        f1 = ttk.Frame(p, width=200, height=100, relief=GROOVE)
        f2 = ttk.Frame(p, width=200, height=100, relief=GROOVE)
        p.add(f1)
        p.add(f2)
        p.grid(column=0, row=0)

    def add_radios(self) -> None:
        """
        Creates the radios on the bottom of the window and implements the logic to make the style change according to
        the selected Radiobutton
        """
        s = ttk.Style()
        s.configure('custom.TRadiobutton', background='blue', foreground='yellow', font='helvetica 8')
        s.map('custom.TRadiobutton', background=[('active', 'blue')])
        tvar = StringVar()
        tvar.set(s.theme_use())
        styles_frame = ttk.Frame(self.root, relief=SUNKEN, padding=(5, 20))
        styles_frame.grid(row=1, column=0, columnspan=2)
        i = 0
        for style in s.theme_names():
            ttk.Radiobutton(styles_frame, text=style, value=style, variable=tvar, style='custom.TRadiobutton',
                            command=lambda: s.theme_use(tvar.get())).grid(row=i, column=0, sticky="W")
            i += 1

    def launch(self) -> None:
        """
        Checks if the window has been launched as a Toplevel or it's a Tk window. If it's a Tk it launches the mainloop.
        """
        self.tk.update()
        if isinstance(self.tk, Tk):
            print("TK detected")
            self.tk.mainloop()


if __name__ == '__main__':
    window = F2window()
    window.launch()
