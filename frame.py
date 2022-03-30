from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('T I T L E')

frame = LabelFrame(root, text="This is my frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="dont click")
b2 = Button(frame, text="...or here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()