# assuming live 90 years
# 1 year = 52 weeks 
# 90 years = 90 * 52 = 4680 weeks

age = int(input("What is your current age?\n"))
age_in_weeks = 52 * age

left_weeks = 4680 - age_in_weeks
print(f"Your age is {age_in_weeks} weeks and you've {left_weeks} weeks in your life.")
