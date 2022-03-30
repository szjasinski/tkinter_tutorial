from tkinter import *

root = Tk()

# creating a label widget
mylabel1 = Label(root, text="Hello World!")
mylabel2 = Label(root, text="to ja szmk")

# shoving it onto the screen
# mylabel.pack()  # makes a window size equal to the size of information within it

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)

root.mainloop()