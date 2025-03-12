# *********************************** PASSWORD STRENGTH CHECKER ***********************************

# Taking user input for the password
password = input("Enter your password: ")

# Checking the length of the password to determine its strength
if len(password) < 6:
    strength = "Weak"  # Passwords shorter than 6 characters are considered weak

elif len(password) < 10:
    strength = "Medium"  # Passwords between 6 and 9 characters are considered medium strength

else:
    strength = "Strong"  # Passwords with 10 or more characters are considered strong

# Displaying the password strength
print(f"Your password is {strength}")
