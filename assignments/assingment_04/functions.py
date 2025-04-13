# Built in Function
print("Hello World") # Print is built in function
length = len("Huzaifa")
print(length)

# User defined Functions
def greeting(name):
    return f"Wellcome! {name}"

print(greeting("Huzaifa"))

# Functions with arguments
def add(num1, num2):
    return num1 + num2

print(add(5, 9))

# Functions with default arguments
def power(number, exponent=2):
    return number ** exponent

print(power(5))
print(power(3, 4))

# Functions with return value
def is_even(num):
    return num % 2 == 0

print(is_even(3))
print(is_even(6))

# Function with keyword argument
def student_data(name, age):
    print(f"Name: {name}, Age: {age}")

student_data("Huzaifa", 18)
student_data(name="Huzaifa", age=18)

# Lambda function
add = lambda numb1, numb2: numb1 + numb2
print(add(4, 8))

mult = lambda x, y: x * y
print(mult(6, 2))

# FUnction with *args
def sum_all(*args):
    return sum(args)

print(sum_all(1, 8, 9, 10, 5))

# Function with **kwargs
def student_detail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
student_detail(name="Huzaifa", age=18, city="Karachi", course="Python")

# Recursive function
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
print(factorial(5))

# Funtion with yield keyword
def even_generator(number):
    for num in range(2, number + 1, 2):
        yield num  # Yield the current even number and pause execution

for i in even_generator(10):  
    print(i)