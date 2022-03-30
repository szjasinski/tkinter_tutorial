# inspired by https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *

root = Tk()
root.title("simple calculator")

e = Entry(root, width=27, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))


def button_click_clear():
    e.delete(0, END)


def button_click_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_click_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_click_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_click_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_click_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


# define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))  # lambda is needed
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))  # to pass argument in function
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=button_click_add)
button_equal = Button(root, text="=", padx=135, pady=20, command=button_click_equal)
button_clear = Button(root, text="C", padx=39, pady=20, command=button_click_clear)
button_subtract = Button(root, text="−", padx=41, pady=20, command=button_click_subtract)
button_multiply = Button(root, text="×", padx=41, pady=20, command=button_click_multiply)
button_divide = Button(root, text="÷", padx=42, pady=20, command=button_click_divide)

# put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_add.grid(row=4, column=0)
button_equal.grid(row=6, column=0, columnspan=3)
button_clear.grid(row=4, column=2)

button_subtract.grid(row=5, column=0)
button_divide.grid(row=5, column=2)
button_multiply.grid(row=5, column=1)

root.mainloop()
