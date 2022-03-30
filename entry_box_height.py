from tkinter import *

root = Tk()
root.title('its my title')
root.geometry("400x400")


def my_click():
    hello = "hello " + e.get()
    my_label = Label(root, text=hello)
    e.delete(0, END)
    my_label.pack()


e = Entry(root, width=50, font=('Helvetica', 54))
e.pack(padx=10, pady=10)

my_btn = Button(root, text="enter your name", command=my_click)
my_btn.pack(pady=10)


root.mainloop()
