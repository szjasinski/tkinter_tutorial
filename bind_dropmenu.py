from tkinter import *
from tkinter import ttk

root = Tk()
root.title('its my title')
root.geometry("400x400")


def selected(event):
    # my_label = Label(root, text=clicked.get()).pack()

    if clicked.get() == 'friday':
        my_label = Label(root, text="nice, piatunio").pack()
    else:
        my_label = Label(root, text=clicked.get()).pack()


def comboclick(event):
    if my_combo.get() == 'friday':
        my_label = Label(root, text="nice, piatunio").pack()
    else:
        my_label = Label(root, text=my_combo.get()).pack()


options = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

my_combo = ttk.Combobox(root, value=options)
my_combo.current(0)
my_combo.bind("<<ComboboxSelected>>", comboclick)
my_combo.pack()

# my_btn = Button(root, text="select from list", command=selected)
# my_btn.pack()

root.mainloop()
