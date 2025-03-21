# ********************************* GENERATOR FUNCTION WITH YIELD *********************************

# Define a generator function that yields even numbers up to the given limit
def even_generator(number):
    # Loop through even numbers from 2 to 'number' (inclusive)
    for num in range(2, number + 1, 2):
        yield num  # Yield the current even number and pause execution

# Iterate over the generator using a for loop
for i in even_generator(10):  # Calls the generator function
    print(i)  # Prints each even number one by one