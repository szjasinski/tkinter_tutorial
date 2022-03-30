from tkinter import *
import time
root = Tk()
root.geometry("600x600")


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")

    my_label.config(text=hour + ":" + minute + ":" + second)
    my_label.after(1000, clock)

    my_label2.config(text=day)

def update():
    my_label.config(text="new text")


my_label = Label(root, text="", font=("Helvetica", 48))
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=("Helvetica", 48))
my_label2.pack(pady=20)

clock()

root.mainloop()