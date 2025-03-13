# Prompt the user to enter a word
user_input = input("Enter the word: ")

# Initialize a flag to track if a non-repeated character is found
found = False

# Loop through each character in the input word
for char in user_input:
    # Check if the character appears only once in the word
    if user_input.count(char) == 1:
        print(f"The non-repeated character is: {char}")
        
        # Set the flag to True since we found a unique character
        found = True
        
        # Exit the loop after finding the first non-repeated character
        break

# If no unique character was found, print the message once
if not found:
    print("There is no non-repeated character")
