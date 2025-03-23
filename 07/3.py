# step 2
import random

# create word list and select one random word from list
word_list = ["makan", "jalan", "beli", "mandi"]
rand_word = random.choice(word_list)



# create empty display list
# loop through every letter in the range of rand_word
# in every loop, add "_" to the diplay list
display = []
for letter in range(len(rand_word)):
    display += "_"
print(display)

# define False
eog = False

# loop through eog variable
# not eog = lawan False is True
while not eog:

    # user guess letter and conver to lower
    guess = input("Input the letter:: ").lower()
    
    for position in range(len(rand_word)):
        letter = rand_word[position]
        if letter == guess:
            display[position] = letter

    # end condition
    # if _ is not in display
    # change eog = True (to end the loop)
    # print you win
    # end of loop
    if "_" not in display:
        eog = True
        print("You win")

    print(display)



    print(guess)
    print(rand_word)

