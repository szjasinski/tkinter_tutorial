from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('T I T L E')

# r = IntVar()  # tkinter variables should match type in radiobutton's variables definition
# r.set("2")

MODES = [
    ("pepperoni", "pepperoni"),
    ("cheese", "cheese"),
    ("mushroom", "mushroom"),
    ("onion", "onion")
]

pizza = StringVar()
pizza.set("pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


# Radiobutton(root, text="option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# my_label = Label(root, text=pizza.get())
# my_label.pack()

my_button = Button(root, text="click me pls", command=lambda: clicked(pizza.get()))
my_button.pack()

mainloop()
