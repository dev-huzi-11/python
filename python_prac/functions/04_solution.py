# ******************************* FINDING AREA AND CIRCUMFERENCE *******************************
# Importing the math module to use the value of pi
import math

# Function to calculate the area and circumference of a circle
def circle_stats(radius):
    # Calculate the area of the circle and round it to 2 decimal places
    area = round(math.pi * radius ** 2, 2)

    # Calculate the circumference of the circle and round it to 2 decimal places
    circumference = round(2 * math.pi * radius, 2)

    # Return both values as a tuple
    return area, circumference

# Calling the function with a radius of 10 and storing the returned values
area, circumference = circle_stats(10)

# Printing the results using formatted strings with newline character '\n'
print(f"Area = {area}\nCircumference = {circumference}")