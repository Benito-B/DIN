from tkinter import *
from tkinter import ttk
import numpy as np
from transformations.Velo3.Speedodom import Speedodom
import threading
import time


def worker():
    b = 240
    while True:
        if b == 0:
            b,l,st = 240,0,-2
        else:
            b,l,st = 0,240,10
        for v in np.arange(b, l, st):
            time.sleep(0.5)
            spd.setspeed(v)



root = Tk()
f = ttk.Frame()
f.pack()
spd = Speedodom(f, width=500, height=400)
spd.grid(row=0, column=0)
t = threading.Thread(target=worker).start()
root.mainloop()



