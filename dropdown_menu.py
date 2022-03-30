from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('here we go')
root.geometry("200x200")  # initial size of the window

# drop down boxes


def show():
    my_label = Label(root, text=clicked.get()).pack()


options = ["one", "two", "three", "four"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_btn = Button(root, text="show selection", command=show).pack()
root.mainloop()
