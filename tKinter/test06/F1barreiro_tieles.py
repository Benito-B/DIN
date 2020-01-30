from tkinter import *
from tkinter import ttk
from test06.F2barreiro_tieles import F2window


class F1window:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Course is almost done")
        self.tk.geometry("600x400-30+30")
        self.tk.resizable(True, True)
        self.tk.minsize(500, 300)
        self.tk.maxsize(700, 500)
        self.root = None
        self.fill()

    def fill(self) -> None:
        ttk.Button(self.root, text="Minimize Window", command=self.minimize).pack()
        ttk.Button(self.root, text="Preferences", command=lambda: F2window(Toplevel(self.root))).pack()
        main_menu = Menu(self.tk)
        window_menu = Menu(main_menu, tearoff=0)
        x_resizable_var = BooleanVar()
        y_resizable_var = BooleanVar()
        x_resizable_var.set(True)
        y_resizable_var.set(True)
        window_menu.add_checkbutton(label="X resizable", var=x_resizable_var,
                                    command=lambda: self.tk.resizable(x_resizable_var.get(), y_resizable_var.get()))
        window_menu.add_separator()
        window_menu.add_checkbutton(label="Y resizable", var=y_resizable_var,
                                    command=lambda: self.tk.resizable(x_resizable_var.get(), y_resizable_var.get()))
        window_menu.add_command(label="Close", command=lambda: self.tk.destroy())
        main_menu.add_cascade(menu=window_menu, label="Window")
        self.tk['menu'] = main_menu

    def minimize(self) -> None:
        self.tk.iconify()

    def launch(self) -> None:
        self.tk.mainloop()


if __name__ == '__main__':
    window = F1window()
    window.launch()
