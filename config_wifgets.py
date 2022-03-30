from tkinter import *

root = Tk()
root.title('Tic Tac Toe')
root.geometry("420x420")

my_frame = Frame(root, width=500, height=500)
my_frame.pack(fill=BOTH, expand=1)


listk = []


def cmd():
    listk[0].config(text="twoja hehe")


button_1 = Button(my_frame, text="xd", font=("Helvetica", 32), padx=55, pady=50, command=cmd)
listk.append(button_1)
listk[0].pack()
print(listk[0])


root.mainloop()
