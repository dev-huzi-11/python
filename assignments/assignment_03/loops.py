# ****************************************** LOOPS ******************************************

# ================= FOR LOOP =================

# Iterating through a list of fruits
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)

# Iterating through each letter in a string
for letter in "Python":
    print(letter)

# Iterating through a dictionary
students = {"name": "Huzaifa", "age": 18, "city": "Karachi"}

# Printing key-value pairs
for item in students.items():
    print(f"item: {item}")

# Printing only keys
for key in students.keys():
    print(f"Key: {key}")

# Printing only values
for value in students.values():
    print(f"Value: {value}")

# Using range() to iterate from 1 to 9
for num in range(1, 10):
    print(num)

# Printing even numbers between 1 and 10
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

# Printing odd numbers using a step of 2
for num in range(1, 11, 2):
    print(num)

# Using 'break' to stop loop execution when num == 5
for num in range(1, 10):
    if num == 5:
        break  # Stops the loop when num is 5
    print(num)

# Using 'continue' to skip the number 5 and continue the loop
for num in range(1, 10):
    if num == 5:
        continue  # Skips 5 and moves to the next iteration
    print(num)

# Nested for loop example (creating pairs of numbers)
for num1 in range(1, 4):  # Outer loop
    for num2 in range(1, 4):  # Inner loop
        print(f"({num1}, {num2})")

# ================= WHILE LOOP =================

# Printing "Joker" until num reaches 10
num = 3
while num <= 10:
    print("Joker")
    num += 1  # Incrementing num to avoid infinite loop

# Taking user input until the user types 'exit'
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter a command (type 'exit' to stop): ")
    print(f"You entered: {user_input}")
