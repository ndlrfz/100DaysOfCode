# math operation order: PEMDAS
# Prentheses -> Exponents -> Multiplication -> Division -> Addition -> Substraction

# user input -> convert to int -> assign to weight
# user input -> convert to float -> assign to height
weight = int(input("Input yur current weight kilogram? ex: 80\n"))
height = float(input("Input your current hright in meter? ex: 1.80\n"))

# BMI formula: wight / height ** 2
bmi = weight / height ** 2
print(round(bmi, 1))
