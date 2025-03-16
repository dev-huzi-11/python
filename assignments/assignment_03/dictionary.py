# **************************************** DICTIONARY ****************************************

# *********** Basic Declaration ***********

car1 = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}

print(car1)

# We can declare key-value pair data using dict
car2 = dict(brand="Honda", model="Civic", year=2019)
print(car2)

# Accessing Values
print(car1["brand"])
print(car1["model"])
print(car1["year"])

print(car2["brand"])
print(car2["model"])
print(car2["year"])

# Adding new item
car1["color"] = "Red"
print(car1)

# Updating an item
car1["year"] = 2021
print(car1)

# Deleting an item
del car1["color"]
print(car1)

# *********** Dictionary Methods ***********

car3 = {"brand": "Ford", "model": "Mustang", "year": 2022}

# Get (to get value from item)
get_data = car3.get("model")
print(get_data)

# items (used to get items from dictionary)
item_data = car3.items()
print(item_data)

# Keys (to get key from dictionary)
keys_data = car3.keys()
print(keys_data)

# Values (to get values from dictionary)
value_data = car3.values()
print(value_data)

# setdefault (set default value if key is missing)
car3.setdefault("brand", "Unknown")  # If key exists, it returns the value
print(car3)

car3.setdefault("engine", "V8")  # If key does not exist, it will be set in dict
print(car3)

# pop (used to remove item from dictionary)
car3.pop("year")
print(car3)

# popitem (used to remove last item)
car3.popitem()
print(car3)

# copy (used to create copy of dictionary)
copy_dict = car3.copy()
print(copy_dict)

# update (used to update the item)
car3.update({"model": "F-150"})
print(car3)

# clear (clear the dictionary)
car3.clear()
print(car3)

# ********* Nested Dictionaries *********

cars_data = {
    "Toyota": {"model": "Camry", "year": 2021},
    "Honda": {"model": "Accord", "year": 2020}
}

print(cars_data)
print(cars_data["Toyota"])
print(cars_data["Toyota"]["year"])

# ******** Iterating over dictionary ********

person_data = {"name": "John", "age": 30, "city": "New York"}

for person in person_data:
    print(person_data[person])

# Looping through key-value pair
for key, value in person_data.items():
    print(key, ":", value)

# Looping through keys
for key in person_data.keys():
    print(key)

# Looping through values
for value in person_data.values():
    print(value)

# Using Condition in dictionary 

if "name" in person_data:
    print("John is a software engineer.")

if person_data.get("name") == "John":
    print("John lives in New York.")

# *********** Dictionary Comprehension ***********
squares = {num: num**2 for num in range(1, 6)}
print(squares)

# ********** Filtering **********

# Filtering senior employees
employees = {"Alice": 25, "Bob": 35, "Charlie": 40}
seniors = {name: age for name, age in employees.items() if age >= 30}
print(seniors)
print(seniors.keys())

# Filtering high scores
students = {
    "Alice": {"marks": 85},
    "Bob": {"marks": 75},
    "Charlie": {"marks": 65}
}

toppers = {name: marks for name, marks in students.items() if marks["marks"] >= 80}
print(toppers)
