# ************************************** POLYMORPHISM **************************************

# Function to multiply two values
def multiply(num1, num2):
    return num1 * num2  # Returns the product of num1 and num2

# Calling the function with two integers
print(multiply(5, 10))  # Output: 50

# Calling the function with a string and an integer (demonstrating polymorphism)
print(multiply("Huzaifa ", 4))  # Output: "Huzaifa Huzaifa Huzaifa Huzaifa" (string repeated 4 times)
