from tkinter import *

root = Tk()
root.title('its my title')
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)


# click command
def our_command():
    my_label = Label(root, text="you clicked menu").pack()


# create a file menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="Copy", command=our_command)

# create an options menu item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find next", command=our_command)


root.mainloop()
