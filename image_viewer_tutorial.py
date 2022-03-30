from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('T I T L E')

# root.iconbitmap('c:/xxx/xxx') # icon for left top corner in Windows programs

my_img1 = ImageTk.PhotoImage(Image.open("image_viewer/hey.png"))  # define img
my_img2 = ImageTk.PhotoImage(Image.open("image_viewer/face1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("image_viewer/face2.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("image_viewer/face3.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(root, text=">>>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<<", command=lambda: back(image_num-1))

    if image_num == 4:
        button_forward = Button(root, text=">>>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    # update status bar
    status = Label(root, text="Image " + str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_num):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1])
    button_forward = Button(root, text=">>>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<<", command=lambda: back(image_num - 1))

    if image_num == 1:
        button_back = Button(root, text="<<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    # update status bar
    status = Label(root, text="Image " + str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<<", state=DISABLED)
button_exit = Button(root, text="EXIT", command=root.quit)
button_forward = Button(root, text=">>>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
