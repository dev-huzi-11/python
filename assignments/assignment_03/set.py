# *************************************** SET ***************************************

# A set is an unordered collection of unique elements.
# Sets are mutable, but their elements must be immutable (e.g., numbers, strings, tuples).

# ************* DECLARATION *************

# Creating a set with unique elements
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Creating a set from a list (duplicates are automatically removed)
duplicate_set = set(["Huzaifa", "Ahsan", "Kashif", "Ahsan"])
print(duplicate_set)  # Output: {'Huzaifa', 'Ahsan', 'Kashif'}

# ************* Methods *************

# Adding an element to the set
my_set.add(6)   # Adds 6 to the set
print(my_set)  # Output: {1, 2, 3, 4, 6}

# Removing an element from the set
# If the element is not found, remove() raises a KeyError
my_set.remove(3)  # Removes 3 from the set
print(my_set)  # Output: {1, 2, 4, 6}

# Discarding an element from the set
# If the element is not found, discard() does nothing (no error)
my_set.discard(10)  # Tries to remove 10 (does nothing since 10 is not in the set)
print(my_set)  # Output: {1, 2, 4, 6}

# Removing a random element from the set (pop removes an arbitrary element)
my_set.pop()  # Removes and returns a random element
print(my_set)  # Output varies since sets are unordered

# Clearing all elements from the set
my_set.clear()  # Removes all elements from the set
print(my_set)  # Output: set()

# ************* Set Operations *************

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union - combines both sets (all unique elements from both A and B)
print(A | B)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection - gets only the common elements between A and B
print(A & B)  # Output: {3, 4}

# Difference - gets elements that are in A but not in B
print(A - B)  # Output: {1, 2}

# Symmetric Difference - gets elements in A or B but not in both
print(A ^ B)  # Output: {1, 2, 5, 6}