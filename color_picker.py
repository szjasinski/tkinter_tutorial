from tkinter import *
from tkinter import colorchooser


root = Tk()
root.title('its my title')
root.geometry("400x400")


def pick_color():
    my_color = colorchooser.askcolor()[1]  # getting hexcolor code
    my_label = Label(root, text=my_color, bg=str(my_color), font=("Helvetica", 32)).pack(pady=10)
    root.configure(bg=str(my_color))


my_btn = Button(root, text="pick color", command=pick_color)
my_btn.pack()

root.mainloop()
