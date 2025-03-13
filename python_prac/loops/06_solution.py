try:
    # Take user input and convert it to an integer
    number = int(input("Enter your number: "))

    fact = 1  # Initialize factorial variable

    # Loop runs while number is greater than 0
    while number > 1:
        fact *= number  # Multiply fact by the current number
        number -= 1  # Decrease number by 1

    # Print the final factorial result
    print(f"Factorial: {fact}")

except ValueError:
    # Handle invalid input (if the user enters a non-integer)
    print("Invalid number")
