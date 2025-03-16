# ******************************************* LIST *******************************************

# ********* BASIC LIST DECLARATION *********

# list of type string
cars_brands = ["Audi", "BMW", "Toyota", "Ferrari"]
print(cars_brands)

# list of type number
numbers = [1, 2, 3, 4]
print(numbers)

# list of multiple type
multi_list = [1, 2, "Apple", True]
print(multi_list)

# ********** Slicing & Indexing **********

fruits = ["Apple", "Mango", "Banana", "Orange"]

# ***** Slicing *****

# positive slicing
print(fruits[2:])
print(fruits[:4])
print(fruits[2:4])

# negative sliing
print(fruits[:-2])
print(fruits[-4:])


# ***** Indexing *****

# positive indexing
print(fruits[1])
print(fruits[3])

# negative indexing
print(fruits[-1])
print(fruits[-3])

# Modifying list using index and slicing
fruits[2] = "Cherry"
print(fruits)

fruits[2:3] = ["Banana"]
print(fruits)


# ********* loop through list *********

for fruit in fruits:
    print(f"My favourite fruit is {fruit}")


# conditional statement in list

if "cherry" in fruits:
    print("cherry is in the basket")
else:
    print("Cherry is not in the basket")


# *********** Methods ***********
months = ["January", "February", "March", "April"]

# append (add value in the end)
months.append("May")
print(months)

# insert (insert value at given index)
months.insert(0, "December")
print(months)

# remove (remove the first occurence)
months.remove("February")
print(months)

# pop (remove the elements at given index)
months.pop(3)
print(months)

# reverse (reverse the list)
months.reverse()
print(months)

# sort (sort the list)
months.sort()
print(months)

# count (return count of given element)
count = months.count("January")
print(count)

# index (return the index of first occurence of element)
index = months.index("May")
print(index)

# copy (create copy of list)
copy = months.copy()
print(copy)

# clear (clear the list)
copy.clear()
print(copy)