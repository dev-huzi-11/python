# ***************************** OPERATORS *****************************

# *********** Arithmetic Operators ***********
# Arithmetic Operator used for basic mathematical calculation

num1 = 10
num2 = 4

# Addition 
print(num1 + num2)

# Subtraction
print(num1 - num2)

# Multiplication
print(num1 * num2)

# Division
print(num1 / num2)

# Floor Division (return floor value)
print(num1 // num2)

# Modulus (return remainder)
print(num1 % num2)

# Exponent
print(num1 ** num2)


# ************ Assignment Operator ************
# Assignment Operator used to assign values to variable

num3 = 6

# +=
num3 += 3
print(num3) 

# -=
num3 -= 3
print(num3)

# *=
num3 *= 4
print(num3)

# /=
num3 /= 2
print(num3)

# %=
num3 %= 7
print(num3)

# //=
num3 //= 2
print(num3)

# **=
num3 **= 3
print(num3)

# &=
num3 = int(num3)
num3 &= 16
print(num3)

# |=
num3 |= 4
print(num3)


# **************** Comparison Operator ****************
# Comparison operators are used to compare two values

num4 = 8
num5 = 3

# Equal
print(num4 == num5)

# Not Equal
print(num4 != num5)

# Greater than
print(num4 > num5)

# Less than
print(num4 < num5)

# Greater than or equal to
print(num4 >= num5)

# Less than or equal to
print(num4 <= num5)


# ***************** Logical Operator *****************
# Logical Operator  Used to combine conditional statements.

x = True
y = False

num6 = 8
num7 = 4

# and
print(x and y)

condition1 = num6 > num7 and num6 == 8
print(condition1)

condition2 = num6 < num7 and num6 > 10
print(condition2)

# or
print(x or y)

condition3 = num6 < num7 or num6 > 2
print(condition3)

# not
print(not x)
print(not y)

condition4 = not condition3
print(condition4)


# ******************** Identity Operator ********************
# Identity Operators are used to check if two variables refer to the same object in memory

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

num8 = 8
num9 = 8

# is
print(num8 is num9)
print(list1 is list2)
print(list1 is list3)

# not
print(num8 is not num9)
print(list1 is not list3)

# ******************** Membership Operators ********************
# Mebership Operators are used to check if a value is in a sequence (like lists, tuples, sets, or strings)

word = "python"
coding_channels = ["chai aur code", "Apna College", "Code with Harry"]

# in
print("Code with Harry" in coding_channels)
print("Pyush Garg" in coding_channels)

# in using loop
for channel in coding_channels:
    print(channel)


for word in word:
    print(word)

# in with conditional statement
user_roles = ["admin", "editor", "manager"]

for role in user_roles:
    print("access granted")
else:
    print("access denied")

# not in
print("Code with Harry" not in coding_channels)
print("Pyush Garg" not in coding_channels)


# *********************** Bitwise Operators ***********************
# Used for bitwise operations.

a = 5  # 0b0101
b = 3  # 0b0011

print(a & b)  # 1  (Bitwise AND → 0101 & 0011 = 0001)
print(a | b)  # 7  (Bitwise OR → 0101 | 0011 = 0111)
print(a ^ b)  # 6  (Bitwise XOR → 0101 ^ 0011 = 0110)
print(~a)     # -6 (Bitwise NOT → ~0101 = -0110)
print(a << 1) # 10 (Left Shift → 0101 << 1 = 1010)
print(a >> 1) # 2  (Right Shift → 0101 >> 1 = 0010)