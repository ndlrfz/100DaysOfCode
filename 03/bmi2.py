# math operation order: PEMDAS
# Prentheses -> Exponents -> Multiplication -> Division -> Addition -> Substraction

# user input -> convert to int -> assign to weight
# user input -> convert to float -> assign to height
weight = int(input("Input yur current weight kilogram:: 70, 80\n"))
height = float(input("Input your current height in meter:: 1.70, 1.80\n"))

# BMI formula: wight / height ** 2
bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you're Underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have Normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you're slightly Overweight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, and you're Obese.")
else:
    print(f"Your BMI is {bmi}, you're Clinically Obsese.")

