# ********************************* TRANSPORTATION MODE SELECTION *********************************

try:
    # Taking user input for distance and converting it to an integer
    distance = int(input("Enter the distance: "))

    # Checking the distance to determine the mode of transportation
    if distance < 3:
        transport = "Walk"  # If distance is less than 3 km, walking is recommended

    elif distance <= 15:
        transport = "Bike"  # If distance is between 4 and 15 km, biking is recommended

    else:
        transport = "Car"  # If distance is greater than 15 km, a car is recommended

    # Displaying the recommended transportation mode
    print("AI recommends you the transport of", transport)

except ValueError:
    # Handling cases where the user enters invalid input (non-numeric values)
    print("Please enter a valid distance")
