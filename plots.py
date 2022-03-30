from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('matplotlib')
root.geometry("400x200")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()


my_btn = Button(root, text="graph it", command=graph)
my_btn.pack()

root.mainloop()
