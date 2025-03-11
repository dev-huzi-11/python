# *********************************** FRUIT RIPENESS CHECKER ***********************************

# Asking the user to input a fruit name
fruit = input("Enter your fruit name: ").lower()

# Checking if the fruit is "Banana" (case-sensitive)
if fruit == "banana":
    
    # Asking the user to enter the color of the fruit
    color = input("Enter your fruit color: ")

    # Checking ripeness based on the color of the banana
    if color == "Green":  
        print(f"Your {fruit} is Unripe")  # Green bananas are unripe
    
    elif color == "Yellow":  
        print(f"Your {fruit} is Ripe")  # Yellow bananas are ripe
    
    elif color == "Brown":  
        print(f"Your {fruit} is Overripe")  # Brown bananas are overripe

    else:
        print(f"Unknown ripeness status for {fruit} with color {color}")  # Handling unexpected colors

# If the fruit is not "Banana", inform the user that it's not supported
else:  
    print(f"Currently not available for {fruit}")
