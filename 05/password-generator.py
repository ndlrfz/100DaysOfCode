# ask users:
# how many letters
# how many symbol to use
# how many number to use
# using random module

# total_other = (jumlah symbol + jumlah number + jumlah CAPS)
# total_letter = max - total_other
# random.sample(list, number of element)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "@", "#", "$", "&", "^", "*"]

ask_letters = int(input("How many letters you wanto:: "))
ask_letters_up = int(input("How many uppercase letters you want:: "))
ask_numbers = int(input("How manu numbers you want:: "))
ask_symbols = int(input("How many symbols you want:: "))

total_letters = list(random.sample(letters, ask_letters))
total_letters_up = list(random.sample(letters_up, ask_letters_up))
total_numbers = list(random.sample(numbers, ask_numbers))
total_symbols = list(random.sample(symbols, ask_symbols))

total_numbers_str = [str(i) for i in total_numbers]

merged_pass = []

for char in [total_letters, total_letters_up, total_numbers_str, total_symbols]:
    merged_pass += char

pass_random = random.shuffle(merged_pass)
pass_final = ''.join(merged_pass)

print(f"Your final password is: {pass_final}, which is {len(pass_final)} characters.")
