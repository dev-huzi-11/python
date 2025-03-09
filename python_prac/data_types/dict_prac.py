# **************************************** DICTIONARY ****************************************

# *********** Basic Declaration ***********

student1 = {
    "name": "Huzaifa",
    "age": 17,
    "institute": "GIAIC"
}

print(student1)

# We can declare key value pair data using dict
student2 = dict(name = "Khuzaima", age = 12, institute = "Crescent")
print(student2)

# Accessing Values
print(student1["name"])
print(student1["age"])
print(student1["institute"])

print(student2["name"])
print(student2["age"])
print(student2["institute"])

# Adding new item
student1["city"] = "Karachi"
print(student1)

# Updating an item
student1["age"] = 18
print(student1)

# Deleting 
del student1["city"]
print(student1)


# *********** Dictionary Methods ***********

student3 = {"name": "Ahsan", "age": 19, "institute": "BBSUL"}

# Get (to get value from item)
get_data = student3.get("name")
print(get_data)

# items (used to get items from dictionary)
item_data = student3.items()
print(item_data)

# Keys (to get key from dictionary)
keys_data = student3.keys()
print(keys_data)

# Values (to get values from dictionary)
value_data = student3.values()
print(value_data)

# setdefault (set default value if key is missing)
student3.setdefault("name", "Unknow")  # If key exist it return the value of
print(student3)

student3.setdefault("city", "Krachi") # If key does not exist it will set this in dict
print(student3)

# pop (used to remove item from dictionary)
student3.pop("age")
print(student3)

# popitem (used to remove last item)
student3.popitem()
print(student3)

# copy (used to create copy of dictionary)
copy_dict = student3.copy()
print(copy_dict)

# update (used to update the item)
student3.update({"name": "Kashif"})
print(student3)

# clear (clear the dictionary)
student3.clear()
print(student3)


# ********* Nested Dictionaries *********

students_data = {
    "Huzaifa": {"age": 17, "institute": "GIAIC"},
    "Ahsan": {"age": 19, "institute": "GIAIC"}
}

print(students_data)
print(students_data["Huzaifa"])
print(students_data["Huzaifa"]["age"])


# ******** Iterating over dictionary ********

teacher_data = {"name": "Asharib", "age": 21, "city": "Nawabshah"}

for teacher in teacher_data:
    print(teacher_data[teacher])

# Looping through key-value pair
for key, value in teacher_data.items():
    print(key, ":", value)

# Looping through key
for key in teacher_data.keys():
    print(key)

# Looping through values
for value in teacher_data.values():
    print(value)


# Using Condition in dictionary 

if "name" in teacher_data:
    print("Sir Asharib is brilliant teacher.")

if teacher_data.get("name") == "Asharib":
     print("Sir Asharib is brilliant teacher.")


# *********** Dictionary Comprehension ***********
squares = {num: num**2 for num in range(1,6)}
print(squares)

# ********** Filtering **********

# Filtering adults
friends = {"Huzaifa": 18, "Ahsan": 19, "Kashif": 17 }
adults = {name: age for name, age in friends.items() if age >= 18}
print(adults) 
print(adults.keys()) 

# Filtering topper
students = {
    "Huzaifa": {"marks": 80},
    "Ahsan": {"marks": 60},
    "Kashif": {"marks": 40}
}

topper = {name: marks for name, marks in students.items() if marks["marks"] >= 70}
print(topper)