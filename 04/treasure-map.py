line1 = ["🔥", "🔥", "🔥"]
line2 = ["🔥", "🔥", "🔥"]
line3 = ["🔥", "🔥", "🔥"]

map = [line1, line2, line3]

user_choice = input("Choose the treasure spot::\n")

letter = user_choice[0].lower()
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(user_choice[1]) - 1

map[number_index][letter_index] = "💧"

print(f"{line1}\n{line2}\n{line3}")



# A = [line1[0], line2[0], line3[0]]
# B = [line1[1], line2[1], line3[1]]
# C = [line1[2], line2[2], line3[2]]
#
# treasure = input("Enter your treasure number::\n")
#
# if treasure == "A1":
#     A[0] = "💧"
# elif treasure == "A2":
#     A[1] = "💧"
# elif treasure == "A3":
#     A[2] = "💧"
# elif treasure == "B1":
#     B[0] = "💧"
# elif treasure == "B2":
#     B[1] = "💧"
# elif treasure == "B3":
#     B[2] = "💧"
# elif treasure == "C1":
#     C[0] = "💧"
# elif treasure == "C2":
#     C[1] = "💧"
# elif treasure == "C3":
#     C[2] = "💧"
#
# print(f"{A}\n{B}\n{C}")
