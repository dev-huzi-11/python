# ******************************************* TUPLE *******************************************

# Declaration

# Tuple of type String
tech_brands = ("Apple", "Samsung", "Google", "Microsoft")
print(tech_brands)

# Tuple of type Numbers
scores = (95, 88, 76, 100)
print(scores)

# Tuple of multiple types
info_tuple = ("Alice", 25, False)
print(info_tuple)


# ************ Indexing & Slicing ************

colors = ("Red", "Blue", "Green", "Yellow")

# Indexing
print(colors[0])
print(colors[1])
print(colors[-1])

# Slicing
print(colors[1:3])
print(colors[:2])
print(colors[1:])
print(colors[:-2])

# ************** Tuple Operation **************
extra_colors = ("Purple", "Orange")

# + operator (used for concatenation)
all_colors = extra_colors + colors
print(all_colors)

# Repetition (duplicates a tuple and links all of them together)
subject = ("Math",)
repeated_subjects = subject * 3
print(repeated_subjects)

# Membership Operator (used to test whether a value or variable exists within a sequence such as a string, list, tuple, or set)

test_tuple = (100, 200, 300, 400)
print(200 in test_tuple)
print(500 in test_tuple)


# **************** Tuple Methods ****************

num_tuple = (5, 10, 10, 20, 25)

# Count (returns the number of times a specified value appears in the tuple)
print(num_tuple.count(10))

# Index (returns the first appearance of a value)
print(num_tuple.index(10))


# ************* Packing & Unpacking *************

# Packing (means assigning multiple values to a tuple)
city_info = ("New York", "USA", 8.4, True)
print(city_info)

# Unpacking (means extracting tuple elements into separate variables)
mobile_brands = ("iPhone", "Samsung Galaxy", "Pixel", "OnePlus")

brand1, brand2, brand3, brand4 = mobile_brands
print(brand1)
print(brand2)
print(brand3)
print(brand4)

# Converting Tuple to List
convert_to_list = list(mobile_brands)
print(convert_to_list)

# Nested Tuple (tuple in tuple)
nested_tuple = (("Alice", 30), ("Bob", 28), ("Charlie", 27))
print(nested_tuple)
print(nested_tuple[0])
print(nested_tuple[0][1])