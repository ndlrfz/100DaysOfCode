print("Your Love Calculator..\n")
name1 = input("Enter your name::\n")
name2 = input("Enter your love name::\n")

names = name1 + name2

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
ll = names.count("l")
o = names.count("o")
v = names.count("v")

total_tl = str((t + r + u + e)) + str((ll + o + v + e))
total_tl_int = int(total_tl)

if total_tl_int < 10 or total_tl_int > 90:
    print(f"Your score is {total_tl_int}, you be like coke and mentos")
elif total_tl_int > 40 and total_tl_int <= 50:
    print(f"Your score is {total_tl_int}, You're alright together")
else:
    print(f"Your score is {total_tl_int}")
