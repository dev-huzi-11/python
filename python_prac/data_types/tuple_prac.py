# ******************************************* TUPLE *******************************************

# Declaration

# Tuple of type String
cars_brands = ("Audi", "Honda", "Toyota", "BMW")
print(cars_brands)

# Tuple of type Numbers
marks = (80, 78, 50, 90)
print(marks)

# Tuple of multiple types
my_tuple = ("Huzaifa", 17, True)
print(my_tuple)


# ************ Indexing & Sliing ************

fruits = ("Banana", "Apple", "Mango", "Cherry")

# Indexing
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# Slicing
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
print(fruits[:-2])

# ************** Tuple Operation **************
more_fruits = ("Watermelon", "Strawberry")

# + operator (used for concatenation)
all_fruits = more_fruits + fruits
print(all_fruits)

# Repitition (duplicates a tuple and links all of them together)
language = ("Python")
rept = language * 3
print(rept)

# Membership Operator (used to test whether a value or variable exists within a sequence such as a string, list, tuple, or set)

tup = (10, 20, 50, 40)
print(20 in tup)
print(80 in tup)


# **************** Tuple Methods ****************

new_tup = (1, 3, 3, 6, 9)

# Count (returns the number of times a specified value appears in the tuple)
print(new_tup.count(3))

# index (return the first appearence)
print(new_tup.index(3))


# ************* Packing & Unpacking *************

# Packing (means assigning multiple values to tuple)
friends = ("Ahsan", "Muslim", "Kashif", 5, 80, True)
print(friends)

# Unpacking (means extracting tuple elements into separate variables)
pct_players = ("Babar", "Shoaib Akhtar", "Wasim Akram", "Amir")

player1, player2, player3, player4 = pct_players
print(player1)
print(player2)
print(player3)
print(player4)

# Converting Tuple to list
convert_to_list = list(pct_players)
print(convert_to_list)

# Nested Tuple (tuple in tuple)
nested_tuple = (("AHsan", 19), ("Saad", 18), ("Kashif", 17))
print(nested_tuple)
print(nested_tuple[0])
print(nested_tuple[0][1])