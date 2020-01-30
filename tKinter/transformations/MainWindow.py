from tkinter import *
from tkinter import ttk
import numpy as np

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

points = [[10, 40], [130, 0], [130, 40]]
triangle = canvas.create_polygon(points, width=2)
current_pos = None


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


def find_triangle_centroid(tri: list) -> list:
    return [(tri[0][0] + tri[1][0] + tri[2][0]) / 3,
            (tri[0][1] + tri[1][1] + tri[2][1]) / 3,
            1]


def move_to_origin(current_form: list) -> list:
    global current_pos
    current_pos = find_triangle_centroid(current_form)
    at_center = np.dot(current_form, translate_matrix([-current_pos[0], -current_pos[1]]))
    return at_center.tolist()


def rotate_in_place(current: list, angles: int) -> list:
    """
    rotates a triangle in place
    @param current: triangle WITHOUT homogenization
    @param angles: angles to rotate
    @return: triangle rotated in place dehomogenized
    """
    t = current[:]
    actualpos = find_triangle_centroid(current)
    print("current:", t)
    in_center = np.dot(current, translate_matrix([-actualpos[0], -actualpos[1]])).dot(rotate(angles))\
        .dot(translate_matrix([actualpos[0], actualpos[1]]))
    return in_center.tolist()


new_triangle = points[:]
homogenize(new_triangle)
move_me_sempai = points[:]
move_me_sempai = rotate_in_place(move_me_sempai, 55)
dehomogenize(move_me_sempai)
print(move_me_sempai)
canvas.create_polygon(move_me_sempai)
moved = move_to_origin(new_triangle)
lista = np.dot(new_triangle, rotate(30)).dot(translate_matrix([50, 50])).tolist()
moved = np.dot(moved, rotate(180)).dot(translate_matrix(current_pos)).tolist()
moved3 = np.dot(moved, translate_matrix([10, 175])).dot(rotate(-45)).tolist()
dehomogenize(moved)
dehomogenize(moved3)
canvas.create_polygon(moved)
canvas.create_polygon(moved3)
dehomogenize(lista)
canvas.create_polygon(lista)
root.mainloop()
