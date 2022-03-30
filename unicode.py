from tkinter import *

root = Tk()
root.title('its my title')
root.geometry("400x400")

my_label = Label(root, text='41' + u'\u00b0', font=("Helvetica", 32)).pack(pady=10)

my_btn = Button(root, text=u'\u00A3', font=("Helvetica", 32)).pack()

root.mainloop()
