from tkinter import *
from tkinter import ttk
import numpy as np

class Speedodom(Canvas):

    def homogenize(self, coords: list):
        for i in range(len(coords)):
            coords[i].append(1)

    def dehomogenize(self, coords: list):
        for i in range(len(coords)):
            coords[i][0] = coords[i][0] / coords[i][2]
            coords[i][1] = coords[i][1] / coords[i][2]
            del coords[i][2]

    def gettranslation(self, tx: float, ty: float) -> list:
        return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

    def getrotation(self, deg: float) -> list:
        rad = np.radians(deg)
        return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]

    def create_oval(self, x, y, r, **options):
        return super().create_oval(x-r, y-r, x+r, y+r, options)

    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.width = int(self.cget('width'))
        self.center = int(self.width / 2)
        self.proportion = float(int(self.cget('width')) * 0.15)

        self.create_oval(self.center, self.center, 15,fill='grey')
        self.create_oval(self.center, self.center, 20,fill='white')

        self.create_oval(self.center, self.center, 25,fill='grey')
        self.create_oval(self.center, self.center, 20,fill='black')

        self.create_text([[200, 235]], text='km/h')
        super().create_oval(90,275,95,280, fill='black')
        short = [[-175, 0],[-150, 0]]
        self.homogenize(short)
        toorig = self.gettranslation(self.center, self.center)
        for rot in range(-20,220,20):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, toorig)
            temp = np.dot(short,transform).tolist()
            self.dehomogenize(temp)
            self.create_line(temp)

        large = [[-175, 0],[-140, 0]]
        self.homogenize(large)
        toorig = self.gettranslation(self.center, self.center)
        for rot in range(-30,220,20):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, toorig)
            temp = np.dot(large,transform).tolist()
            self.dehomogenize(temp)
            self.create_line(temp)

        pos = [[-120, 0]]
        self.homogenize(pos)
        toorig = self.gettranslation(self.center, self.center)
        vel = 0
        for rot in range(-30,220,20):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, toorig)
            temp = np.dot(pos,transform).tolist()
            self.dehomogenize(temp)
            self.create_text(temp, text=str(vel))
            vel = vel + 20

        needle = [[0,0], [-7, -7], [0, -150], [7, -7]]
        self.homogenize(needle)
        toorig = self.gettranslation(self.center, self.center)
        rotation = self.getrotation(-123)
        transform = np.dot(rotation, toorig)
        needle2 = np.dot(needle,transform).tolist()
        self.dehomogenize(needle2)
        self.create_polygon(needle2, outline='#f11', fill='#1f1', width=2)
