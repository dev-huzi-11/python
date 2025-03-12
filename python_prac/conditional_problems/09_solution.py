# ************************************** LEAP YEAR CHECKER **************************************

# Taking user input for the year and converting it to an integer
year = int(input("Enter year: "))

# Checking if the year is a leap year
# A year is a leap year if:
# 1. It is divisible by 400 (e.g., 2000, 2400)
# OR
# 2. It is divisible by 4 but not by 100 (e.g., 2024, 2028)
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")  # If the condition is met, the year is a leap year
else:
    print(f"{year} is not a leap year")  # Otherwise, it is not a leap year