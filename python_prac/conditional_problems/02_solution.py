# ********************************** MOVIE TICKET PRICING **********************************

try:
    # Asking user for their age and converting it to an integer
    user_age = int(input("Enter your age: "))

    # Asking for the movie
    movie = input("Enter movie name: ")

    # Asking for the day of the week and converting it to lowercase for consistency
    day = input("Enter day: ").lower()

    # Setting ticket price: $12 for adults (age > 18), $8 for minors (age <= 18)
    price = 12 if user_age > 18 else 8

    # Checking if the day is Wednesday for a $2 discount
    if day == "wednesday":
        discounted_price = price - 2  # Applying discount
        print(f"Your ticket price for {movie} movie is {discounted_price}$")  # Displaying discounted price
    else:
        print(f"Your ticket price for {movie} movie is {price}$")  # Displaying regular price

except ValueError:
    # Handling invalid age input (non-numeric values)
    print("Enter a valid age.")