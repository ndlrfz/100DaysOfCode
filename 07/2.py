# step 2
import random

# create word list and select one random word from list
word_list = ["makan", "jalan", "beli", "mandi"]
rand_word = random.choice(word_list)

# user guess letter and conver to lower
guess = input("Input the letter:: ").lower()

# loop through new list
for letter in rand_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

# create an empty list
# loop through every letter
# every loop adding character
# if character == guess, add the guess letter
# else add "_"
# new_list = []
# for letter in rand_word:
#     if letter == guess:
#         new_list.append(letter)
#     else:
#         new_list.append("_")

# create empty display list
# loop through every letter in the range of rand_word
# in every loop, add "_" to the diplay list
display = []
for letter in range(len(rand_word)):
    display += "_"
print(display)

for position in range(len(rand_word)):
    letter = rand_word[position]
    if letter == guess:
        display[position] = letter

print(display)
print(guess)
print(rand_word)
#print(type(new_list))

