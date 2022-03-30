from tkinter import *

root = Tk()
root.title('its my title')
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)


# click command
def our_command():
    my_label = Label(root, text="you clicked menu").pack()


# hide all frames
def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


# file new function
def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    my_label = Label(file_new_frame, text="you clicked New").pack()


# edit cut
def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    my_label = Label(edit_cut_frame, text="you clicked Cut").pack()


# create a file menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_command)

# create an options menu item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find next", command=our_command)

# create some frames
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")


root.mainloop()
