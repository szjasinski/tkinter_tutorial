from tkinter import *

root = Tk()
root.title('its my title')
root.geometry("400x400")


def clicker(event):
    my_label = Label(root, text="you clicked")
    my_label.pack()
    print("ok")


my_btn = Button(root, text="click pls")
# my_btn.bind("<Enter>", clicker)  # activate after moving mouse to the button
my_btn.bind("<Leave>", clicker)
my_btn.pack(pady=20)


root.mainloop()
