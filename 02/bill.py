print("Welcome to the Bill and Tip calculator")

total = float(input("What is the amount of total bill?\n"))
tip = int(input("What is percentage of Tip you want to give? ex: 10, 12, 15\n"))
person = int(input("How many person on the table?\n"))

tip_total = total * (tip / 100)
total_bill = total + tip_total

pay_per_person = total_bill / person

print(f"Each person should pay ${float(round(pay_per_person, 3))}.")
