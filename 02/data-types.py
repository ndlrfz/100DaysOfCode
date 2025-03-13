# convert user input to string via str()
# assign to variable num_input
num_input = str(input("Enter your number?\n"))

# extract the user input with [0] - index
num1 = num_input[0]
num2 = num_input[1]

# the operation add num1 as integer + num2 as integer
# assign to hasil variable
hasil = int(num1) + int(num2)
# print hasil
print(f"Hasil penjumlahan dari {num_input} adalah: {hasil}")
