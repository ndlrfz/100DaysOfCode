pizza_choice = input("Enter your Pizza choice:: L/M/S\n")

price = 0

if pizza_choice == "L":
    price += 25
elif pizza_choice == "M":
    price += 20
else:
    price += 15

peperoni = input("Do you want to add Peperoni? Y/N\n")

if peperoni == "Y":
    if pizza_choice == "S":
        price += 2
    else:
        price += 3

cheese = input("Do you want to add Cheese? Y/N\n")

if cheese == "Y":
    price += 1

print(f"Your final price is: {price}")

