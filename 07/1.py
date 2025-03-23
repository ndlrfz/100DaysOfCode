# step 1
import random

# create word list and select one random word from list
word_list = ["makan", "jalan", "beli", "mandi"]
rand_word = random.choice(word_list)

# user guess letter and conver to lower
guess = input("Input the letter:: ").lower()

# make the chosen word as str
# create new list from str choosen
rand_str = rand_word[0]
rand_list = list(rand_str)

# loop through new list
for letter in rand_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

print(rand_word)
print(guess)
