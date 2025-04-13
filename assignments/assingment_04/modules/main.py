# Built-in module
import math  # full import of module
sqrt_result = math.sqrt(4)
print("Square root of 4 is:", sqrt_result)

# Importing a specific function from a built-in module
from math import pow
power_result = pow(2, 3)  # 2 raised to the power of 3
print("2 to the power of 3 is:", power_result)

# User-defined module (assuming script.py exists in the same directory and has an 'addition' function)
from script import addition
sum_result = addition(4, 9)
print("Sum of 4 and 9 is:", sum_result)

# Third-party module with alias (make sure 'requests' is installed using pip)
import requests as req
response = req.get("https://api.github.com")
print("GitHub API status code is:", response.status_code)