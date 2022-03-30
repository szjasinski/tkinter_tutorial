from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('T I T L E')

# root.iconbitmap('c:/xxx/xxx') # icon for left top corner in Windows programs

my_img = ImageTk.PhotoImage(Image.open("hey.png"))  # define img
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()
