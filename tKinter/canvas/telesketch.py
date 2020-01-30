from tkinter import *
from tkinter import ttk

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.resizable(False, False)

cur_x, cur_y = 150, 150


def addLine(di: str):
    global canvas
    global cur_x, cur_y
    line_lenght = 10
    if di == "left":
        canvas.create_line((cur_x, cur_y, cur_x - line_lenght, cur_y))
        cur_x -= line_lenght
    elif di == "right":
        canvas.create_line((cur_x, cur_y, cur_x + line_lenght, cur_y))
        cur_x += line_lenght
    elif di == "up":
        canvas.create_line((cur_x, cur_y, cur_x, cur_y - line_lenght))
        cur_y -= line_lenght
    elif di == "down":
        canvas.create_line((cur_x, cur_y, cur_x, cur_y + line_lenght))
        cur_y += line_lenght


top_frame = ttk.Frame(root, width=300, height=300, relief=RAISED)
top_frame.grid(column=0, row=0, sticky=(N, W, E, S))

canvas = Canvas(top_frame)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
scroll_x = ttk.Scrollbar(top_frame, orient="horizontal", command=canvas.xview)
scroll_x.grid(row=1, column=0, sticky="ew")
scroll_y = ttk.Scrollbar(top_frame, orient="vertical", command=canvas.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

bottom_frame = ttk.Frame(root, width=300, height=75, relief=SUNKEN, padding=(10, 0))
bottom_frame.grid(column=0, row=1, sticky=(N, W, E, S))
button_canvas = Canvas(bottom_frame, width=300, height=75)
button_canvas.grid(column=0, row=0, sticky=(N, W, E, S))
# Left arrow
points = [0, 40, 30, 10, 30, 70]
arrow_left = button_canvas.create_polygon(points, width=2)
# Right arrow
points = [40, 70, 40, 10, 70, 40]
arrow_right = button_canvas.create_polygon(points, width=2)
# Up arrow
points = [220, 40, 250, 10, 280, 40]
arrow_up = button_canvas.create_polygon(points, width=2)
# Down arrow
points = [220, 45, 280, 45, 250, 75]
arrow_down = button_canvas.create_polygon(points, width=2)
button_canvas.tag_bind(arrow_left, "<Button-1>", lambda e: addLine("left"))
button_canvas.tag_bind(arrow_right, "<Button-1>", lambda e: addLine("right"))
button_canvas.tag_bind(arrow_up, "<Button-1>", lambda e: addLine("up"))
button_canvas.tag_bind(arrow_down, "<Button-1>", lambda e: addLine("down"))
root.bind("<Left>", lambda e: addLine("left"))
root.bind("<Right>", lambda e: addLine("right"))
root.bind("<Up>", lambda e: addLine("up"))
root.bind("<Down>", lambda e: addLine("down"))
root.update()
root.mainloop()
