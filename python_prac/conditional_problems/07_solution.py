# ***************************************** COFFEE CUSTOMIZATION *****************************************

# Taking user input for coffee type and formatting it properly
coffee = input("Enter your coffee: ").strip().title()

# Taking user input for coffee size and ensuring it's properly formatted
coffee_size = input("Enter your coffee size (small/medium/large): ").strip().lower()

# Asking the user if they want an extra shot and converting input to lowercase for consistency
extra_shot = input("Do you want an extra shot? (Yes/No): ").strip().lower()

# Constructing the order based on user input
if extra_shot == "yes":
    order = f"{coffee_size.capitalize()} {coffee} coffee with an extra shot"
else:
    order = f"{coffee_size.capitalize()} {coffee} coffee"

# Displaying the final order confirmation
print(f"Your order of {order} has been placed.")
