# List of numbers both positive and negative
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10] 

# Storing count of positive number in the variable
positive_numbers = 0 

# Loop through each number in list
for num in numbers:
    # checking if number is positive
    if num > 0:
        positive_numbers += 1 # Increment the counter 1

# Print the total count of positive number 
print(f"Total positive numbers are: {positive_numbers}")