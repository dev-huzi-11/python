# ******************************************* LIST *******************************************

# ********* BASIC LIST DECLARATION *********

# List of Type String
fruits = ["Banana", "Mango", "Cherry"]
print(fruits)

# List of Type Number
marks = [70, 50, 30, 99]
print(marks)

# List with Multiple Data Types
multi_list = ["Huzaifa", 17, True, [1, 2, 3]]
print(multi_list)

# Nested List (List inside a List)
nested_list = [1, 2, 3, [1, 2, 3], [9, 8, 7]]
print(nested_list)

# ********** INDEXING & SLICING **********
idx_slc_list = ["Huzaifa", "Ahsan", "Kashif"]

# ******** Indexing ********

# Positive Indexing (Starts from 0)
print(idx_slc_list[0])  # First element
print(idx_slc_list[1])  # Second element
print(idx_slc_list[2])  # Third element

# Negative Indexing (Starts from -1, counting backward)
print(idx_slc_list[-1])  # Last element
print(idx_slc_list[-2])  # Second last element
print(idx_slc_list[-3])  # Third last element

# ********** Slicing **********

# Positive Slicing (Extract a sublist)
print(idx_slc_list[1:])   # From index 1 to end
print(idx_slc_list[:2])   # From start to index 2 (excluding index 2)
print(idx_slc_list[1:2])  # From index 1 to 2 (excluding 2)

# Negative Slicing
print(idx_slc_list[:-1])  # Exclude the last element
print(idx_slc_list[-1:])  # Get only the last element
print(idx_slc_list[-3:-1])  # From third last to second last


# **************** Changing value in list ****************
cars_brands = ["Audi", "BMW", "Toyota", "Honda", "Hyundai"]
print(cars_brands)

# Replacing an item using indexing
cars_brands[1] = "Suzuki"
print(cars_brands)

# Replacing an item using slicing (Incorrect Approach)
cars_brands[1:2] = "Lamborghini"
print(cars_brands)  # This will break the word into separate characters

# Correct way to replace using slicing (Wrap in a list)
cars_brands[1:2] = ["Lamborghini"]
print(cars_brands)

# ********** Looping through a List **********
forces = ["Army", "Navy", "Air Force", "Rangers"]

# Using a for-in loop
for force in forces:
    print(force)

# ********** Using if-else with Lists **********
cities = ["Karachi", "Lahore", "Islamabad", "Hyderabad"]

# Check if an item exists in the list
if "Rawalpindi" in cities:
    print("Rawalpindi is a beautiful city.")
else:
    print("The city does not exist.")

if "Karachi" in cities:
    print("Karachi is the city of lights.")
else:
    print("The city does not exist.")


# ************************ List Methods ************************

tea_varieties = ["Black", "Ginger", "Green"]
print(tea_varieties)

# Append (Add one item at the end of the list)
tea_varieties.append("Herbal")
print(tea_varieties)

# Pop (Remove last element of the list)
tea_varieties.pop()
print(tea_varieties)

# Insert (Insert an item at a given index)
tea_varieties.insert(2, "Oolong")
print(tea_varieties)

# Remove (Remove a specific item from the list)
tea_varieties.remove("Green")
print(tea_varieties)

# Index (Find the index of an item)
tea_index = tea_varieties.index("Ginger")
print(tea_index)

# Extend (Merge two lists)
extra_varieties = ["White", "Masala"]
tea_varieties.extend(extra_varieties)
print(tea_varieties)

# Sort (Arrange elements in ascending order)
tea_varieties.sort()
print(tea_varieties)

# Reverse (Reverse the order of the list)
tea_varieties.reverse()
print(tea_varieties)

# Count (Return the total occurrences of an item)
tea_count = tea_varieties.count("Black")
print(tea_count)

# Copy (Create a copy of the original list)
copy_list = tea_varieties.copy()
print(copy_list)

# We can use all methods and logic on the copied list
# Example:
copy_list.append("Herbal")
print(copy_list)

# Clear (Remove all items from the list)
tea_varieties.clear()
print(tea_varieties)