year = int(input("Enter year to check::\n"))

# Solution with and operator
# if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print(f"Year {year} is a Leap year.")
# else:
#     print(f"Year {year} is Not Leap year.")

# Solution with Nested if else
# if all condition must be true
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is a Leap year")
        else:
            print(f"Year {year} is Not Leap year")
    else:
        print(f"Year {year} is a Leap year")
else:
    print(f"Year {year} is Not Leap year")
