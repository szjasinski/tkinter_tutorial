from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0, "enter you name")


def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


my_button = Button(root, text="ok", padx=50, command=my_click)
my_button.pack()

root.mainloop()
