from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('here we go')
root.geometry("200x200")  # initial size of the window


def show():
    my_label = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="check it pls", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_button = Button(root, text="show selection", command=show).pack()
my_label = Label(root, text=var.get()).pack()

root.mainloop()
