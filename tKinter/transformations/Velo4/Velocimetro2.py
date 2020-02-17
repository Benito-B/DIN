from tkinter import *
from tkinter import ttk
import numpy as np
from Speedodom import Speedodom
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
            # spd1.setspeed(v)
            # spd2.setspeed(v)
            # spd3.setspeed(v)
            # spd4.setspeed(v)
    return
root = Tk()
f = ttk.Frame(root)
f.pack()
spd1 = Speedodom(f, width=400, height=400)
spd1.grid(row=0, column=0)
spd2 = Speedodom(f, width=300, height=300)
spd2.grid(row=0, column=1)
spd3 = Speedodom(f, width=200, height=200)
spd3.grid(row=1, column=0)
spd4 = Speedodom(f, width=500, height=500)
spd4.grid(row=1, column=1)
t = threading.Thread(target=worker).start()
root.mainloop()



