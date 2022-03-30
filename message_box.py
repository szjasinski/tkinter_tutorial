from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('T I T L E')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.askyesno("this is my popup", "hello world, its szmk")
    Label(root, text=response).pack()
    # 1 for yes/ok, 0 for no/cancel
    if response == 1:
        Label(root, text="you clicked yes").pack()
    if response == 0:
        Label(root, text="you clicked no").pack()


Button(root, text="popup", command=popup).pack()

root.mainloop()
