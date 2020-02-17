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

    def getscaled(self, xscl:float, yscl:float) -> list:
        return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]

    def setspeed(self, vel:float):
        print(vel)
        if vel < -5 or vel > 240: return
        self.delete(self.lastneedle)
        needle = [[0,0], [-7, -7], [0, -150], [7, -7]]
        self.homogenize(needle)
        toorig = self.gettranslation(200, 200)
        rotation = self.getrotation((240*vel/240)-120)
        transform = np.dot(rotation, toorig)
        needle2 = np.dot(needle,transform)
        needle2 = np.dot(needle2, self.scale).tolist()
        self.dehomogenize(needle2)
        self.lastneedle = self.create_polygon(needle2, outline='#f11', fill='#1f1', width=2)

    def create_circle(self, x, y, r, **options) -> int:
        return super().create_oval(x-r, y-r, x+r, y+r, options)

    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.w0 = 400
        self.h0 = 400

        self.lastneedle = None

        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.xscl = self.w / self.w0
        self.yscl = self.h / self.h0

        self.scale = self.getscaled(self.xscl, self.yscl)

        temp = [[15, 15, 1],[385, 385, 1]]
        temp = np.dot(temp, self.scale).tolist()
        self.dehomogenize(temp)
        self.create_oval(temp, fill='grey')

        temp = [[20, 20, 1], [380, 380, 1]]
        temp = np.dot(temp, self.scale).tolist()
        self.dehomogenize(temp)
        self.create_oval(temp, fill='white')

        temp = [[175, 175, 1], [225, 225, 1]]
        temp = np.dot(temp, self.scale).tolist()
        self.dehomogenize(temp)
        self.create_oval(temp, fill='grey')

        temp = [[180, 180, 1], [220, 220, 1]]
        temp = np.dot(temp, self.scale).tolist()
        self.dehomogenize(temp)
        self.create_oval(temp, fill='black')

        temp = [[90, 275, 1], [95, 280, 1]]
        temp = np.dot(temp, self.scale).tolist()
        self.dehomogenize(temp)
        self.create_oval(temp, fill='black')

        temp = [[200, 235, 1]]
        temp = np.dot(temp, self.scale).tolist()
        self.dehomogenize(temp)
        self.create_text(temp, text='km/h')

        short = [[-175, 0],[-150, 0]]
        self.homogenize(short)
        toorig = self.gettranslation(200, 200)
        for rot in range(-20,220,20):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, toorig)
            temp = np.dot(short,transform)
            temp = np.dot(temp,self.scale).tolist()
            self.dehomogenize(temp)
            self.create_line(temp)

        large = [[-175, 0],[-140, 0]]
        self.homogenize(large)
        toorig = self.gettranslation(200, 200)
        for rot in range(-30,230,20):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, toorig)
            temp = np.dot(large,transform)
            temp = np.dot(temp, self.scale).tolist()
            self.dehomogenize(temp)
            self.create_line(temp)

        pos = [[-120, 0]]
        self.homogenize(pos)
        toorig = self.gettranslation(200, 200)
        vel = 0
        for rot in range(-30,230,20):
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, toorig)
            temp = np.dot(pos,transform)
            temp = np.dot(temp, self.scale).tolist()
            self.dehomogenize(temp)
            self.create_text(temp, text=str(vel))
            vel = vel + 20

        self.setspeed(-5)

        temp = [[200, 260, 1]]
        temp = np.dot(temp, self.scale).tolist()
        temp2 = [[50, 30, 1]]
        sctemp = self.getscaled(self.xscl, 1)
        temp2 = np.dot(temp2, sctemp).tolist()
        self.dehomogenize(temp)
        self.dehomogenize(temp2)
        velset = IntVar()
        entry = ttk.Entry(master, textvariable=velset)
        entry.bind('<Return>', lambda e: self.setspeed(float(velset.get())))
        self.create_window(temp, width=temp2[0][0], height=temp2[0][1] , window=entry)

