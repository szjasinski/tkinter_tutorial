from tkinter import *

root = Tk()
root.title('its my title')
root.geometry("800x600")

# my_canvas = Canvas(root, width=300, height=200, bg="yellow")
# my_canvas.pack(pady=20)
#
# # rectangle
# # x1, y1 TOP LEFT
# # x2, y2 BOT RIGHT
# my_canvas.create_rectangle(50, 150, 250, 50, fill="green")
#
# # create oval
# my_canvas.create_oval(50, 150, 250, 50, fill="cyan")
#
# # create line
# # x1, y1, x2, y2, fill="color"
# my_canvas.create_line(0, 100, 300, 100, fill="red")
# my_canvas.create_line(150, 0, 150, 200, fill="red")
#
######################################################################################
#####################################################################################
#
# # MOVING SHAPES ON CANVAS
# w = 600
# h = 400
# x = w // 2
# y = h // 2
#
# my_canvas = Canvas(root, width=w, height=h, bg="yellow")
# my_canvas.pack()
#
# my_circle = my_canvas.create_oval(x, y, x + 10, y + 10)
#
#
# def left(event):
#     x = -10
#     y = 0
#     my_canvas.move(my_circle, x, y)
#
#
# def right(event):
#     x = 10
#     y = 0
#     my_canvas.move(my_circle, x, y)
#
#
# def up(event):
#     x = 0
#     y = -10
#     my_canvas.move(my_circle, x, y)
#
#
# def down(event):
#     x = 0
#     y = 10
#     my_canvas.move(my_circle, x, y)
#
#
# def pressing(event):
#     x = 0
#     y = 0
#     if event.char == "a": x = -10
#     if event.char == "d": x = 10
#     if event.char == "w": y = -10
#     if event.char == "s": y = 10
#     my_canvas.move(my_circle, x, y)
#
#
# root.bind("<Key>", pressing)
#
# root.bind("<Left>", left)
# root.bind("<Right>", right)
# root.bind("<Up>", up)
# root.bind("<Down>", down)
#
######################################################################################
#####################################################################################
#
# MOVING IMAGE ON CANVAS
#
w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root, width=w, height=h, bg="yellow")
my_canvas.pack()

img = PhotoImage(file="img/red_pawn_white_bg.png")
my_image = my_canvas.create_image(0, 0, anchor=NW, image=img)


def left(event):
    x = -20
    y = 0
    my_canvas.move(my_image, x, y)


def right(event):
    x = 20
    y = 0
    my_canvas.move(my_image, x, y)


def up(event):
    x = 0
    y = -20
    my_canvas.move(my_image, x, y)


def down(event):
    x = 0
    y = 20
    my_canvas.move(my_image, x, y)


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)


root.mainloop()
