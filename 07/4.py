# step 2
import random

# define the ascii art
HANGMAN = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# create word list and select one random word from list
word_list = ["makan", "jalan", "beli", "mandi"]
rand_word = random.choice(word_list)

# live counter of guess
# max 6 - based on the asciiart list
lives = 6

# define False
eog = False

print("""
You only have 6 lives. Be careful!
Each wrong = lives - 1

""")

# create empty display list
# loop through every letter in the range of rand_word
# in every loop, add "_" to the diplay list
display = []
for letter in range(len(rand_word)):
    display += "_"

print(display)
print(rand_word)

# loop through eog variable
# not eog = lawan False is True
while not eog:

    # user guess letter and conver to lower

    guess = input("Input the letter:: ").lower()
    
    for position in range(len(rand_word)):
        letter = rand_word[position]
        if letter == guess:
            display[position] = letter

    # check if guess is not in the rand_word
    # decrease lives by 1
    # if lives 0 - exit the program and print lose
    if guess not in rand_word:
        lives -= 1
        print(f"You have {lives} lives.")
        if lives == 0:
            eog = True
            print("You Lose!")


    # end condition
    # if _ is not in display
    # change eog = True (to end the loop)
    # print you win
    # end of loop
    if "_" not in display:
        eog = True
        print("You Win!")

    print(display)

    # print HANGMAN
    print(HANGMAN[lives])



