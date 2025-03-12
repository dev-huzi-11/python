# ************************************* PET FOOD RECOMMENDATION *************************************

# Taking user input for pet type and formatting it properly
pet = input("Enter your pet type (Dog/Cat): ").strip().lower()

try:
    # Taking user input for pet's age and converting it to an integer
    age = int(input("Enter your pet's age: "))

    # Checking the pet type and recommending food accordingly
    if pet == "dog":
        if age <= 2:            
            print("Recommended puppy food")  # For dogs aged 2 years or less
        else:
            print("Recommended senior dog food")  # For dogs older than 2 years

    elif pet == "cat":
        if age <= 5:
            print("Feed milk to your cat")  # For cats aged 5 years or less
        else:
            print("Recommended senior cat food")  # For cats older than 5 years

    else:
        print("Enter a valid pet type (either Dog or Cat).")  # Handling invalid pet types

except ValueError:
    print("Please enter a valid age.")  # Handling non-numeric age inputs
