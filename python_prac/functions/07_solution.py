# ************************************** FUNCTION WITH ARGS **************************************

# Define a function that takes an unlimited number of arguments
def sum_all(*args):  
    # The built-in sum() function calculates the total sum of all arguments
    return sum(args)  

# Example usage: Calling the function with different numbers of arguments
print(sum_all(2, 5))         # Output: 7  (2 + 5)
print(sum_all(2, 5, 10))     # Output: 17 (2 + 5 + 10)
print(sum_all(2, 5, 11, 6))  # Output: 24 (2 + 5 + 11 + 6)``