from tkinter import *

root = Tk()
root.title('its my title')
root.geometry("400x400")


class Elder:

    def __init__(self, master):
        my_frame = Frame(master)
        my_frame.pack()

        self.my_button = Button(master, text="click me", command=self.clicker)
        self.my_button.pack(pady=20)

    def clicker(self):
        print("ITS CLICKED")


e = Elder(root)

root.mainloop()
