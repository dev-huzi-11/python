# ********************************** RECURSIVE FUNCTION **********************************

# Define a recursive function to calculate the factorial of a number
def factorial(num):
    if num == 0:  # Base case: Factorial of 0 is 1
        return 1
    else:
        return num * factorial(num - 1)  # Recursive case: num * factorial(num-1)
    
# Call the function and print the result
print(factorial(4))  # Output: 24
