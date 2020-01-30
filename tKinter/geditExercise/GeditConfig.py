from tkinter import *
from tkinter import ttk


class ConfigWindow:

    def __init__(self, t: Toplevel):
        self.window = t
        self.window.title('Config options')
        root = ttk.Label(self.window)
        root.pack(padx=20, pady=20)
        # Style configuration
        s = ttk.Style()
        current_theme = StringVar()
        s.configure('.', background='gray',
                    font='helvetica 16')  # Turns everything white in the current style (Default)
        base_frame = ttk.Frame(root)
        base_frame.pack(fill=X)
        style_frame = ttk.Frame(root)
        style_frame.pack(fill=X)
        # Creating the "options" notebook in the first frame
        notebook = ttk.Notebook(base_frame)
        self.frame_menu_view = ttk.Frame(notebook)
        self.fill_view_menu()
        self.frame_menu_view.grid(column=0, row=0, sticky="NSWE")
        self.frame_menu_editor = ttk.Frame(notebook)
        self.fill_editor_menu()
        self.frame_menu_editor.grid(column=0, row=0, sticky="NSWE")
        notebook.add(self.frame_menu_view, text="View")
        notebook.add(self.frame_menu_editor, text="Editor")
        notebook.grid(column=0, row=0, sticky="NSWE")
        # Creating the style frame
        combo = ttk.Combobox(style_frame, values=s.theme_names(), textvar=current_theme)
        combo.pack(pady=(30, 0))
        combo.bind('<<ComboboxSelected>>', lambda e: s.theme_use(current_theme.get()))
        s.theme_use("clam")
        s.configure('BoldLabel.Label', font='helvetica 14 bold')
        combo.set('clam')

    def sync_margin(self, v: StringVar, w: Spinbox) -> None:
        w.configure(state=v.get())

    def fill_view_menu(self) -> None:
        view_frame = self.frame_menu_view
        ttk.Checkbutton(view_frame, text="Show line numbers").grid(row=0, column=0, sticky="W", padx=10)
        margin_var = StringVar()
        ttk.Checkbutton(view_frame, text="Show right column margin: ", var=margin_var, onvalue="normal",
                        offvalue="disabled", command=lambda: self.sync_margin(margin_var, margin_spin))\
            .grid(row=1, column=0, sticky="W", padx=10)
        margin_spin = Spinbox(view_frame, from_=1.0, to=100.0, width=5)
        margin_spin.configure(state='disabled')
        margin_spin['state'] = 'disabled'
        margin_spin.grid(row=1, column=1, sticky="W", padx=10)
        ttk.Checkbutton(view_frame, text="Show status bar").grid(row=2, column=0, sticky="W", padx=10)
        ttk.Checkbutton(view_frame, text="Show general view map").grid(row=3, column=0, sticky="W", padx=10)
        ttk.Checkbutton(view_frame, text="Show grid").grid(row=4, column=0, sticky="W", padx=10)
        ttk.Label(view_frame, text="Text config", style="BoldLabel.Label").grid(row=5, column=0, pady=(15, 0),
                                                                                sticky="W",
                                                                                padx=25)
        ttk.Checkbutton(view_frame, text="Enable text adjustment").grid(row=6, column=0, sticky="W", padx=10)
        ttk.Checkbutton(view_frame, text="Don't split words").grid(row=7, column=0, sticky="W", padx=10)
        ttk.Label(view_frame, text="Highlights", style="BoldLabel.Label").grid(row=8, column=0, pady=(15, 0),
                                                                               sticky="W",
                                                                               padx=25)
        ttk.Checkbutton(view_frame, text="Highlight current line").grid(row=9, column=0, sticky="W", padx=10)
        ttk.Checkbutton(view_frame, text="Highlight current bracket pair").grid(row=10, column=0, sticky="W", padx=10)

    def fill_editor_menu(self) -> None:
        editor_frame = self.frame_menu_editor
        ttk.Label(editor_frame, text="Indentation", style="BoldLabel.Label").grid(row=0, column=0, pady=(15, 0),
                                                                                  sticky="W",
                                                                                  padx=25)
        ttk.Label(editor_frame, text="Spaces in a tab: ").grid(row=1, column=0, sticky="W", padx=(10, 0))
        Spinbox(editor_frame, from_=1.0, to=10.0, width=5).grid(row=1, column=1, sticky="W")
        ttk.Checkbutton(editor_frame, text="Use spaces isntead of tabulations").grid(row=2, column=0, sticky="W",
                                                                                     padx=10)
