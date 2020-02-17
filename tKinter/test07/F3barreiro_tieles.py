from tkinter import *
from tkinter import ttk
import numpy as np


class Simon(Canvas):

    BASE_WIDTH = 350
    BASE_HEIGHT = 350

    def __init__(self, master=None, **options):
        if not options.get('width'):
            options['width'] = self.BASE_WIDTH
        if not options.get('height'):
            options['height'] = self.BASE_HEIGHT
        super().__init__(master, options)
        self.master = master
        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))
        self.scale_x = self.w / self.BASE_WIDTH
        self.scale_y = self.h / self.BASE_HEIGHT
        self.score = None
        self.create_ui()

    def create_ui(self) -> None:
        scale = self.scalate(self.scale_x, self.scale_y)
        # Creating the main circles
        self.create_circle([[5, 5, 1], [345, 345, 1]], scale, "grey")
        self.create_circle([[10, 10, 1], [340, 340, 1]], scale, "black")
        self.create_circle([[110, 110, 1], [240, 240, 1]], scale, "silver")
        # Creating the circular middle button
        self.create_circle([[165, 180, 1], [185, 200, 1]], scale, "black")
        # Create red circle manually so I can add the bind to it
        tmp = np.dot([[167, 182, 1], [183, 198, 1]], scale).tolist()
        self.dehomogenize(tmp)
        pid = self.create_oval(tmp, fill="red")
        self.tag_bind(pid, '<Button-1>', lambda e: self.score.set(0))
        # Creating the circular left button
        outter_circle = [[165, 180, 1], [185, 200, 1]]
        moved_outter_circle = np.dot(outter_circle, self.translate(-35, 0)).tolist()
        self.create_circle(moved_outter_circle, scale, "black")
        inner_circle = [[167, 182, 1], [183, 198, 1]]
        moved_inner_circle = np.dot(inner_circle, self.translate(-35, 0)).tolist()
        self.create_circle(moved_inner_circle, scale, "yellow")
        # Creating the circular right button
        outter_circle = [[165, 180, 1], [185, 200, 1]]
        moved_outter_circle = np.dot(outter_circle, self.translate(35, 0)).tolist()
        self.create_circle(moved_outter_circle, scale, "black")
        inner_circle = [[167, 182, 1], [183, 198, 1]]
        moved_inner_circle = np.dot(inner_circle, self.translate(35, 0)).tolist()
        self.create_circle(moved_inner_circle, scale, "cyan")
        # Creating big text
        self.draw_text([[175, 150, 1]], scale, 'SIMÓN', 'Arial 23 bold')
        # Creating smaller texts
        self.draw_text([[175, 175, 1]], scale, 'prefs')
        moved_text = np.dot([[175, 175, 1]], self.translate(-35, 0)).tolist()
        self.draw_text(moved_text, scale, 'new')
        moved_text = np.dot([[175, 175, 1]], self.translate(35, 0)).tolist()
        self.draw_text(moved_text, scale, 'scores')
        # Creating the coloured polygons
        base_polygon = [[-70, -10], [-150, -10], [-150, -60], [-60, -150], [-10, -150], [-10, -70], [-30, -70], [-70, -30]]
        self.homogenize(base_polygon)
        colors = (('green4', 'green3'), ('cyan4', 'cyan3'), ('red4', 'red3'), ('yellow4', 'yellow3'))
        for i in range(4):
            poly = np.dot(base_polygon, self.rotate(i*90)).dot(scale).dot(self.translate(self.w/2, self.h/2)).tolist()
            self.dehomogenize(poly)
            pid = self.create_polygon(poly, fill=colors[i][0], activefill=colors[i][1])
            self.tag_bind(pid, '<Enter>', lambda e: self.increase_score())
        # Adding the label
        self.score = IntVar()
        label = ttk.Label(self.master, textvariable=self.score, relief='groove', background='black',
                          foreground='red', anchor='e')
        tmp = np.dot([[175, 220, 1]], scale).tolist()
        self.dehomogenize(tmp)
        self.create_window(tmp, width=60, height=20, window=label)

    def increase_score(self):
        self.score.set(self.score.get() + 10)

    def draw_text(self, pos: list, scale, s: str, font: str = 'Arial 8 bold'):
        tmp = np.dot(pos, scale).tolist()
        self.dehomogenize(tmp)
        self.create_text(tmp, text=s, font=font)

    def create_circle(self, pos: list, scale, fill: str) -> None:
        tmp = np.dot(pos, scale).tolist()
        self.dehomogenize(tmp)
        self.create_oval(tmp, fill=fill)

    def homogenize(self, coords: list) -> None:
        for i in range(len(coords)):
            coords[i].append(1)

    def dehomogenize(self, coords: list) -> None:
        for i in range(len(coords)):
            coords[i][0] = coords[i][0] / coords[i][2]
            coords[i][1] = coords[i][1] / coords[i][2]
            del coords[i][2]

    def translate(self, tx: float, ty: float) -> list:
        return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

    def rotate(self, deg: float) -> list:
        rad = np.radians(deg)
        return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]

    def scalate(self, xscl:float, yscl:float) -> list:
        return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]
