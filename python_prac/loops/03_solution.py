try:
    # Prompt the user to enter a number for the multiplication table
    user_input = int(input("Enter the number of table you want: "))

    # Loop from 1 to 10 to generate the multiplication table
    for table in range(1, 11):
        # Skip the multiplication for 5 using the 'continue' statement
        if table == 5:
            continue
        
        # Calculate the multiple of the user_input number
        multiple = user_input * table
        
        # Print the multiplication result
        print(f"{user_input} x {table} = {multiple}")

# Handle the case where the user enters a non-numeric value
except ValueError:
    print("Please enter a valid number")