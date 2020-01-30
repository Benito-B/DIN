from tkinter import *
import numpy as np


def homogenize(coords: list) -> None:
    for i in range(len(coords)):
        coords[i].append(1)


def dehomogenize(coords: list) -> None:
    for i in range(len(coords)):
        if coords[i][2] > 1:
            for j in range(2):
                coords[i][j] = int(coords[i][j] / coords[i][2])
        coords[i] = coords[i][:2]


def translate_matrix(t: list) -> list:
    return [[1, 0, 0],
            [0, 1, 0],
            [t[0], t[1], 1]]


def rotate(degrees: int) -> list:
    rad = np.radians(degrees)
    return [[np.cos(rad), np.sin(rad), 0],
            [-np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]]


def draw_line(line: list, ang: int) -> None:
    li = np.dot(line, rotate(ang)).dot(translate_matrix([160, 160])).tolist()
    dehomogenize(li)
    global canvas
    canvas.create_line(li, width=2)


def rotate_in_place(current: list, angles: int) -> list:
    """
    rotates a triangle in place
    @param current: triangle WITHOUT homogenization
    @param angles: angles to rotate
    @return: triangle rotated in place dehomogenized
    """
    center_pos = [160, 160]
    in_center = np.dot(current, translate_matrix([-center_pos[0], -center_pos[1]])).dot(rotate(angles))\
        .dot(translate_matrix([center_pos[0], center_pos[1]]))
    return in_center.tolist()


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("320x320")
root.resizable(False, False)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

center = 160

canvas.create_oval(center-155, center-155, center+155, center+155, width=3)
canvas.create_oval(center-25, center-25, center+25, center+25, width=2, outline="blue", fill="lime")
needle = [[center, center], [center-7, center+80], [center, center+100], [center+7, center+80]]
homogenize(needle)
needle = np.dot(needle, translate_matrix([0, -100])).tolist()
needle = rotate_in_place(needle, -120)
dehomogenize(needle)
canvas.create_polygon(needle, width=2, outline="red", fill="lime")
short_line = [[-150, 0], [-125, 0]]
large_line = [[-150, 0], [-115, 0]]

homogenize(large_line)
homogenize(short_line)
for angle in range(-30, 220, 20):
    draw_line(large_line, angle)
    if angle < 210:
        draw_line(short_line, angle+10)

root.mainloop()
