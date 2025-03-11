# Importing the random module to generate a random number
import random

# Displaying welcome messages and game instructions
print("Welcome to the number guessing game.")
print("You have to guess a number between 50 to 100.")
print("You have 5 attempts to guess.")
print("Let's Start!")

# Generating a random number between 50 and 100 that the user has to guess
number_to_guess = random.randint(50, 100)

# Setting the total number of attempts allowed
total_attempts = 5

# Keeping track of the number of attempts the user has used
user_attempts = 0

# Starting the guessing loop, which runs until the user reaches the maximum attempts
while user_attempts < total_attempts:
    
    # Incrementing the attempt counter each time the user makes a guess
    user_attempts += 1
    
    # Taking user input and converting it to an integer
    try:
        user_guess = int(input("Enter your number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number")
        continue
    
    # Checking if the guessed number is correct
    if user_guess == number_to_guess:
        print(f"🎉 Congratulations! {user_guess} is the correct number, and you found it in {user_attempts} attempts.")
        break  # Exiting the loop as the correct number is guessed

    # Giving hints if the guessed number is lower than the actual number
    elif user_guess < number_to_guess:
        print(f"The number {user_guess} is too low. Try again!")
    
    # Giving hints if the guessed number is higher than the actual number
    elif user_guess > number_to_guess:
        print(f"The number {user_guess} is too high. Try again!")

# If the user has used all attempts and hasn't guessed correctly, reveal the number
if user_guess != number_to_guess:
    print(f"Oops! The correct number was {number_to_guess}. Better luck next time.")
