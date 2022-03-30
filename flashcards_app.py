from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('its my title')
root.geometry("500x500")


# create state flashcard function
def states():
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_frame, text="something").pack()


# create state capital slashcard function
def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_capitals_frame, text="something else").pack()


# hide all previous frames
def hide_all_frames():
    # loop thru and destroy all children in previous frames
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()
    state_capitals_frame.pack_forget()


# create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

# create geography menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)


#create our frames
state_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500)


root.mainloop()