# Prompt the user to enter a string
user_input = input("Enter the string: ")

# Initialize an empty string to store the reversed result
reversed_string = ""

# Loop through each character in the user input
for char in user_input:
    # Prepend the current character to the reversed_string
    # This builds the reversed string character by character
    reversed_string = char + reversed_string

# Print the reversed string
print(reversed_string)
