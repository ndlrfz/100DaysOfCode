import random

names = input("Please enter list of  4 names? \n")
list_names = names.split(", ")

gen_number = random.randint(0, len(list_names) - 1)

print(f"{list_names[gen_number]} will pay the bill")

