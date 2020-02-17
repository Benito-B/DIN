from tkinter import *
import numpy as np


def homogenize(coords: list) -> list:
    for i in range(len(coords)):
        coords[i].append(1)
    return coords


def dehomogenize(coords: list) -> list:
    for i in range(len(coords)):
        if coords[i][2] > 1:
            for j in range(2):
                coords[i][j] = int(coords[i][j] / coords[i][2])
        coords[i] = coords[i][:2]
    return coords


def translate(t: list) -> list:
    return [[1, 0, 0],
            [0, 1, 0],
            [t[0], t[1], 1]]


def rotate(degrees: int) -> list:
    rad = np.radians(degrees)
    return [[np.cos(rad), np.sin(rad), 0],
            [-np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]]


def draw_line(line: list, ang: int, vel: int = None) -> None:
    li = np.dot(line, rotate(ang)).dot(translate([160, 160])).tolist()
    dehomogenize(li)
    global canvas
    canvas.create_line(li, width=2)
    if vel is not None:
        t = [[-105, 0]]
        homogenize(t)
        txt_place = np.dot(t, rotate(ang)).dot(translate([160, 160])).tolist()
        dehomogenize(txt_place)
        canvas.create_text(txt_place, text=str(vel))


def rotate_in_place(current: list, angles: int) -> list:
    """
    rotates a triangle in place
    @param current: triangle
    @param angles: angles to rotate
    @return: triangle rotated in place
    """
    center_pos = [160, 160]
    in_center = np.dot(current, translate([-center_pos[0], -center_pos[1]])).dot(rotate(angles)) \
        .dot(translate([center_pos[0], center_pos[1]]))
    return in_center.tolist()


def transform(c: list, a):
    return np.dot(c, a).tolist()


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("320x320")
root.resizable(False, False)

center = 160
min_degs = -30
max_degs = 220
cur_degs = -30

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
# Build circles and needle
canvas.create_oval(center - 158, center - 158, center + 158, center + 158, width=1)
canvas.create_oval(center - 155, center - 155, center + 155, center + 155, width=1)
canvas.create_oval(center - 15, center - 15, center + 15, center + 15, width=1)
canvas.create_text(center, center + 25, text="Km/h")
needle = [[center, center], [center - 7, center + 80], [center, center + 100], [center + 7, center + 80]]
homogenize(needle)
needle = transform(needle, translate([0, -100]))
needle = rotate_in_place(needle, -120)
dehomogenize(needle)
canvas_needle = canvas.create_polygon(needle, width=2, outline="red", fill="lime")
short_line = [[-150, 0], [-125, 0]]
large_line = [[-150, 0], [-115, 0]]

# Build speedometer lines
homogenize(large_line)
homogenize(short_line)
speed = 0
for angle in range(-30, 220, 20):
    draw_line(large_line, angle, speed)
    speed += 20
    if angle < 210:
        draw_line(short_line, angle + 10)


def accelerate(degs: int):
    global needle
    global canvas
    global canvas_needle
    global min_degs, max_degs, cur_degs
    if cur_degs + degs in range(min_degs, max_degs):
        homogenize(needle)
        if cur_degs == 210 and degs > 0:
            degs -= degs * 2
        needle = rotate_in_place(needle, degs)
        dehomogenize(needle)
        canvas.delete(canvas_needle)
        canvas_needle = canvas.create_polygon(needle, width=2, outline="red", fill="lime")
        cur_degs += degs


root.bind('<Right>', lambda e: accelerate(5))
root.bind('<Left>', lambda e: accelerate(-5))

root.mainloop()
