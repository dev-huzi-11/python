# ***************************************** NUMBERS ******************************************
import math
import random

# 1: int
num1 = 2
num2 = 4

# BASIC OPERATION
print(num1 + num2)
print(num2 - num1)
print(num1 * num2)
print(num1 ** num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

# TYPE CHECKING
print(type(num1))
print(type(num2))

# CONVERTING TO INTEGER
print(int(2.4))
print(int("123"))
print(int(True))
print(int(False))

# 2: float
num3 = 2.7
num4 = 5.6

# BASIC OPERATION
print(num3 + num4)
print(num4 - num3)
print(num3 * num4)
print(num3 ** num4)
print(num3 / num4)
print(num3 // num4)
print(num3 % num4)

# ROUNDOFF AND PRECISION
print(round(num3 + num4))
print(format(3.14159, ".3"))
print(format(3.14159, ".2f"))

# CONVERTING TO FLOAT
print(float(8))
print(float("2"))
print(float(True))

# COMPLEX NUMBERS
num5 = 2 + 3j
num6 = 3 + 6j

# BASIC OPERATION 
print(num5 + num6)
print(num5 - num6)
print(num5 * num6)  # (a+bj)×(c+dj)=(ac−bd)+(ad+bc)j
print(num5 / num6)  # (a+bj) / (c+dj)​ = (a+bj)×(c−dj) / (c+dj)×(c−dj)

# MATH FUNCTIONS

# MIN
num7 = 45
num8 = 32
print(min(num7, num8))

# MAX
num9 = 46
num10 = 23
print(max(num10, num9))

# POW
num11 = 4
num12 = 2
print(pow(num11, num12))

# ROUND
num13 = 21.6555534
num14 = 2
print(round(num13, num14))



# ***************************************** MATH ******************************************

# ******** BASIC METHODS *********

# SQRT
sqrt = math.sqrt(64)
print(int(sqrt))

# FACTORIAL
factorail_num = math.factorial(5)
print(factorail_num)

# PI
pi_num = math.pi
print(pi_num, 2)
print(round(pi_num, 2))

# CEIL
ciel_num = math.ceil(54.7)
print(ciel_num)

# FLOOR
floor_num = math.floor(5.8)
print(floor_num)

# GCD
gcd_num = math.gcd(8, 6)
print(gcd_num)

# FSUM
sum_num = math.fsum([1, 3, 5])
print(sum_num)

# FMOD
mod_num = math.fmod(15, 2)
print(mod_num)

# ************************************* RANDOM *************************************

# **** BASIC MRTHODS ****
# RANDOM
random_num1 = random.random()
print(random_num1)

# RANDINT
random_num2 = random.randint(1, 10)
print(random_num2)

# UNIFORM
random_num3 = random.uniform(2, 34)
print(random_num3) 

# CHOICE
random_num4 = [1, 4, 5, 9]
print(random.choice(random_num4))