try:
    number = int(input("Enter your number: "))
    is_prime = True  # Assume the number is prime

    if number <= 1:
        is_prime = False  # Numbers <= 1 are not prime
    else:
        for num in range(2, number):  # Check divisibility from 2 to number-1
            if number % num == 0:
                is_prime = False  # If divisible, it's not prime
                break  # Exit loop early

    # Print result
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

except ValueError:
    print("Invalid number, please enter an integer.")
