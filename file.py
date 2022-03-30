from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('here we go')


def open_file():
    global my_image
    # return location of the file
    root.filename = filedialog.askopenfilename(initialdir="/Users/szymon/PycharmProjects", title="select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="open file", command=open_file).pack()

root.mainloop()
