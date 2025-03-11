# *********************** AGE GROUP CATEGORIZATION ***********************

try:
    # Taking user input and converting it to an integer
    user_age = int(input("Enter your age: "))

    # Checking the age group category
    
    if user_age < 13:  # If the user's age is less than 13
        print("You are a child.")  

    elif user_age < 19:  # If the user's age is between 13 and 18 (inclusive)
        print("You are a teenager.") 

    elif user_age < 59:  # If the user's age is between 19 and 58 (inclusive)
        print("You are an adult.")  

    else:  # If the user's age is 59 or older
        print("You are a senior.")  

except ValueError:  
    # Handling cases where the user enters a non-integer value
    print("Enter a valid age.")
