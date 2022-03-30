from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random


root = Tk()
root.title('its my title')
root.geometry("500x600")


# create randomizing state function
def random_state():
    # create a list of state names
    global our_states
    our_states = ['usa', 'poland', 'russia', 'egypt', 'france', 'italy', 'norway']

    # generate a random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = our_states[rando] + ".png"

    # create our state images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state.config(image=state_image)


# create state capital answer function
def state_capital_answer():
    if capital_radio.get() == our_state_capitals[answer]:
        response = "Correct! " + our_state_capitals[answer].title() + " is the capital of " + answer.title() + "."
    else:
        response = "Incorrect"

    answer_label_capitals.config(text=response)

# create answer function
def state_answer():
    answer = answer_input.get().lower()
    answer = answer.replace(" ", "")

    # determine if our answer is right or wrong
    if answer == our_states[rando]:
        response = "Correct! It was " + our_states[rando].title() + "."
    else:
        response = "Incorrect! "

    answer_label.config(text=response)

    # clear the entry box
    answer_input.delete(0, END)
    random_state()


# create state flashcard function
def states():
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_frame, text="States").pack()

    '''
    # create a list of state names
    global our_states
    our_states = ['usa', 'poland', 'russia']

    # generate a random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = our_states[rando] + ".png"

    # create our state images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    '''

    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady=15)
    random_state()

    # create answer input box
    global answer_input
    answer_input = Entry(state_frame, font=("Helvetica", 18), bd=2)
    answer_input.pack(pady=15)

    # create button to randomize state images
    rando_button = Button(state_frame, text="pass", command=states)
    rando_button.pack(pady=10)

    # create button to answer the question
    answer_button = Button(state_frame, text="answer", command=state_answer)
    answer_button.pack(pady=5)

    # create a label to tell us if we got the answer right or not
    global answer_label
    answer_label = Label(state_frame, text="", font=("Helvetica", 18))
    answer_label.pack(pady=15)


# create state capital flashcard function
def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH, expand=1)
    # my_label = Label(state_capitals_frame, text="Capitals").pack()

    global show_state
    show_state = Label(state_capitals_frame)
    show_state.pack(pady=15)

    global our_states
    our_states = ['usa', 'poland', 'russia', 'egypt', 'france', 'italy', 'norway']

    global our_state_capitals
    our_state_capitals = {
        'usa': 'washington',
        'poland': 'warsaw',
        'russia': 'moscow',
        'egypt': 'cairo',
        'france': 'paris',
        'italy': 'rome',
        'norway': 'oslo'
    }

    # generate a random number
    global rando

    # create empty answer list and counter
    answer_list = []
    count = 1
    global answer

    # generate three random capitals
    while count < 4:
        rando = randint(0, len(our_states) - 1)
        # if first selection, make it our answer
        if count == 1:
            answer = our_states[rando]
            global state_image
            state = our_states[rando] + ".png"
            state_image = ImageTk.PhotoImage(Image.open(state))
            show_state.config(image=state_image)

        # add our first selection to a new list
        answer_list.append(our_states[rando])

        # remove from old list
        our_states.remove(our_states[rando])

        # shuffle original list
        random.shuffle(our_states)
        count += 1

    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(our_state_capitals[answer_list[0]])

    capital_radio_butto1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]].title(), variable=capital_radio, value=our_state_capitals[answer_list[0]]).pack()
    capital_radio_butto2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]].title(), variable=capital_radio, value=our_state_capitals[answer_list[1]]).pack()
    capital_radio_butto3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]].title(), variable=capital_radio, value=our_state_capitals[answer_list[2]]).pack()

    # add a pass button
    pass_button = Button(state_capitals_frame, text="pass", command=state_capitals)
    pass_button.pack(pady=15)

    # create a button to answer
    capital_answer_button = Button(state_capitals_frame, text="answer", command=state_capital_answer)
    capital_answer_button.pack(pady=15)

    # create an answer label
    global answer_label_capitals
    answer_label_capitals = Label(state_capitals_frame, text="", font=("Helvetica", 18))
    answer_label_capitals.pack(pady=15)

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
