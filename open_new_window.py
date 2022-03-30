from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('here we go')


def open_window():
    global my_img

    top = Toplevel()
    top.title('the bsmnt')
    my_img = ImageTk.PhotoImage(Image.open("image_viewer/face1.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="open second window", command=open_window).pack()

root.mainloop()
