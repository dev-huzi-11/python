# Define the limit up to which we want to sum even numbers
n = 10

# Initialize a variable to store the sum of even numbers
sum_even = 0

# Loop through numbers from 1 to n (inclusive)
for num in range(1, n + 1):
    # Check if the current number is even
    if num % 2 == 0:
        # Add the even number to sum_even
        sum_even += num

# Print the sum of even numbers
print(f"The sum of even numbers is: {sum_even}")
