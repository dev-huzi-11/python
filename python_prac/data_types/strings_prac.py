# ********************************************* STRING *********************************************

# ************ BASIC STRING DECLARATION ************

# Single Quotation String
greeting_single1 = 'Hello' 
print(greeting_single1)

greeting_single2 = 'Hello my name is "Huzaifa"'
print(greeting_single2)

# Double Quotation String
greeting_double1 = "Hello, World"
print(greeting_double1)

greeting_double2 = "It's my job to complete this task."
print(greeting_double2)

# Triple Quotation String (Multiline or Docstring)
name_single = '''Huzaifa'''
print(name_single)

name_full = """Huzaifa Nazeer"""
print(name_full)

full_intro = '''My name is Huzaifa.
I'm 17 years old
I'm frontend developer'''
print(full_intro)


# ************ INDEXING & SLICING ************

# Positive Indexing
text1 = "Hello World"
print(text1[0])  # H

# Negative Indexing
text2 = "Hello World"
print(text2[-1])  # d

# Full String Slicing
text3 = "Governor Initiative"
print(text3[:])  # Governor Initiative

# Slicing from Index 9 to End
text4 = "Governor Initiative for AI"
print(text4[9:])  # Initiative for AI

# Slicing First 5 Characters
fruit1 = "Watermelon"
print(fruit1[:5])  # Water

# Slicing a Specific Range
fruit2 = "Banana & Orange"
print(fruit2[7:13])  # Orange

# Negative Indexing for Slicing
fruit3 = "Cherry"
print(fruit3[-5:])  # herry
print(fruit3[:-5])  # C
print(fruit3[1:-1])  # herr

# Reverse a String
print(fruit3[::-1])  # yrrehC


# ************** STRING OPERATIONS **************

# Concatenation
first_word = "Hello"
second_word = "World"

concatenated_string = first_word + " " + second_word
print(concatenated_string)  # Hello World

# Repetition
repeat_text = "Python "
print(repeat_text * 3)  # Python Python Python


# ***************** STRING METHODS *****************

# Capitalize First Letter
user1 = "huzaifa"
print(user1.capitalize())  # Huzaifa

# Convert to Lowercase
user2 = "HUZAIFA"
print(user2.lower())  # huzaifa

# Convert to Uppercase
user3 = "khuzaima"
print(user3.upper())  # KHUZAIMA

# Casefold (Similar to Lowercase but More Aggressive)
user4 = "KHUZAIMA"
print(user4.casefold())  # khuzaima

# Title Case (Capitalizes Each Word)
full_name = "huzaifa nazeer"
print(full_name.title())  # Huzaifa Nazeer

# Swap Case (Uppercase to Lowercase and Vice Versa)
swap_name = "huzaifa nazeer"
print(swap_name.swapcase())  # HUZAIFA NAZEER

# Length of String
short_name = "Anas"
print(len(short_name))  # 4

# Removing Leading and Trailing Spaces
fruit4 = "   Watermelon   "
print(fruit4.strip())  # Watermelon

# Removing Leading Spaces
fruit5 = "   Banana   "
print(fruit5.lstrip())  # Banana   

# Removing Trailing Spaces
fruit6 = "   Cherry   "
print(fruit6.rstrip())  #    Cherry

# Find Substring Position
fruits = "banana, mango, apple"
print(fruits.find("mango"))  # 8

# Reverse Find (Last Occurrence)
multiple_fruits = "Mango, Banana, Banana"
print(multiple_fruits.rfind("Banana"))  # 15

# Index of a Substring
fruit_list = "Cherry, Watermelon, Mango"
print(fruit_list.index("Mango"))  # 18

# Replace Substring
fruit_replacement = "Orange, Apple, Cherry"
print(fruit_replacement.replace("Apple", "Banana"))  # Orange, Banana, Cherry

# Split String into List
car_brands = "Audi, BMW, Lexus, Toyota"
print(car_brands.split(", "))  # ['Audi', 'BMW', 'Lexus', 'Toyota']

clothing_brands = "Gul Ahmed#MTJ#J."
print(clothing_brands.split("#"))  # ['Gul Ahmed', 'MTJ', 'J.']
print(clothing_brands.split("#", 1))  # ['Gul Ahmed', 'MTJ#J.']

# Join List into String
fruit_names = ["Banana", "Mango", "Cherry"]
joined_fruits = " - ".join(fruit_names)
print(joined_fruits)  # Banana - Mango - Cherry

# Startswith Method
introduction = "My name is Huzaifa"
print(introduction.startswith("My"))  # True
print(introduction.startswith("Huzaifa"))  # False

# Endswith Method
bio = "Myself Huzaifa Nazeer"
print(bio.endswith("Nazeer"))  # True
print(bio.endswith("Huzaifa"))  # False

# Center String with Padding
teacher_name = "Asharib"
print(teacher_name.center(30))  # Adds spaces around "Asharib"
print(teacher_name.center(30, "*"))  # Adds * around "Asharib"

# Check if String Contains Only Alphabets
alpha_string = "Huzaifa"
print(alpha_string.isalpha())  # True

# Check if String Contains Only Digits
digit_string = "12345"
print(digit_string.isdigit())  # True

# Check if String is Alphanumeric (Letters and Numbers)
username = "huzaifadev11"
print(username.isalnum())  # True

# Check if String is Only Spaces
space_check = " "
print(space_check.isspace())  # True

# Check If String is Lowercase or Uppercase
lower_name = "huzaifa"
print(lower_name.islower())  # True

upper_name = "HUZAIFA"
print(upper_name.isupper())  # True