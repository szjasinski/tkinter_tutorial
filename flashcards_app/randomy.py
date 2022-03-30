from random import randint
import random

answer_list = []

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

'''
rando = randint(0, len(our_states)-1)

print(our_state_capitals[our_states[rando]])

answer = our_states[rando]

# add our first random selection to our answer_list
answer_list.append(our_states[rando])


# remove answer from list
our_states.remove(our_states[rando])

# shuffle our original list
random.shuffle(our_states)

# randomnly select our next state
rando = randint(0, len(our_states)-1)
answer_list.append(our_states[rando])

# remove 2nd answer from list
our_states.remove(our_states[rando])

# shuffle our original list
random.shuffle(our_states)

# randomnly select our third state
rando = randint(0, len(our_states)-1)
answer_list.append(our_states[rando])

print(answer_list)
print(answer)
'''

count = 1

while count < 4:
    rando = randint(0, len(our_states) - 1)
    # if first selection, make it our answer
    if count == 1:
        answer = our_states[rando]

    # add our first selection to a new list
    answer_list.append(our_states[rando])

    # remove from old list
    our_states.remove(our_states[rando])

    # shuffle original list
    random.shuffle(our_states)

    count +=1


print(answer_list)
print(answer)
print(our_state_capitals[our_states[rando]])
