from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('here we go')
root.geometry("200x200")  # initial size of the window


def my_click(var):
    global my_label

    my_label.grid_forget()
    my_label = Label(root, text=str(horizontal.get()) + "x" + str(vertical.get()))
    my_label.grid(row=2, column=0, columnspan=2)
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


vertical = Scale(root, from_=200, to=500, command=my_click)  # cant pack slider in one line, errors later
vertical.grid(row=0, column=0)

# horizontal = Scale(root, from_=200, to=500, orient=HORIZONTAL)


# to react while sliding, slide function need argument
horizontal = Scale(root, from_=100, to=400, orient=HORIZONTAL, command=my_click)
horizontal.grid(row=0, column=1)

my_btn = Button(root, text="click me", command=my_click)
my_btn.grid(row=1, column=0, columnspan=2, pady=10)

my_label = Label(root, text=str(horizontal.get()) + "x" + str(vertical.get()))
my_label.grid(row=2, column=0, columnspan=2)


root.mainloop()
