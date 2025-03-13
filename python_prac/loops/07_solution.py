while True:  # Infinite loop to keep asking for input until valid input is provided
    try:
        # Taking user input and converting it to an integer
        num = int(input("Enter number between 1 to 10: "))

        # Checking if the number is within the valid range
        if 1 <= num <= 10:
            print("Thanks")  # Valid input, exit the loop
            break
        else:
            print("Invalid number")  # Number is out of range, ask again

    except ValueError:
        # Handles cases where input is not a valid integer (e.g., letters, symbols)
        print("Please enter a valid number.")
