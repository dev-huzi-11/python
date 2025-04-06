# OOP (Object-Oriented Programming)

OOP stands for **Object-Oriented Programming**. It is a programming paradigm that organizes code using **Classes** and **Objects**, where data (attributes) and actions (methods) are grouped together to model real-world entities.

---

## Class

A **class** is a **blueprint** or **template** for creating **objects**. It defines the structure and behavior that the objects created from it will have. A class usually contains:
- **Attributes** (properties/data)
- **Methods** (functions/actions)

### **For example**:

```python
class Car:
    def __init__(self, brand, model):
        self.name = brand  # Attribute (name)
        self.model = model  # Attribute (model)

    def drive(self):  # Method (action)
        print(f"The {self.name} {self.model} is the best.") 

# Creating objects from the Car class
car1 = Car("Audi", "R8")  # car1 is an object of the Car class
car1.drive()  # Output: Audi R8 is the best.

car2 = Car("BMW", "i8")  # car2 is another object of the Car class
car2.drive()  # Output: BMW i8 is the best.
```

---

## Constructor

A **constructor** is a special method in a class, usually named `__init__()`, that is called **automatically** when an object is created. It is used to **initialize** the attributes of an object. Every time you create a new object from a class, the constructor runs to set up that object with initial values.

### **For example**:

```python
class Car:
    def __init__(self, brand, model):
        # The constructor is called when an object is created
        self.name = brand  # Initializes the attribute 'name'
        self.model = model  # Initializes the attribute 'model'

    def drive(self):
        print(f"The {self.name} {self.model} is driving!")  # Uses the attributes to print info

car1 = Car("Audi", "R8")  # The constructor runs here
car1.drive()  # Output: The Audi R8 is driving!
```

- The `__init__()` constructor automatically sets up the `name` and `model` attributes for each car object.

---

## Attributes

**Attributes** are the **data** or **properties** associated with an object. They are often referred to as **fields** or **variables** in some programming languages. Attributes define the characteristics of an object.

In the above example:
- **`name`** and **`model`** are attributes of the `Car` class.
- When an object is created, these attributes are initialized with values (like "Audi" and "R8" for `car1`).

### **For example**:

```python
class Car:
    def __init__(self, brand, model):
        self.name = brand  # name is an attribute
        self.model = model  # model is an attribute

car1 = Car("Audi", "R8")
print(car1.name)  # Output: Audi (accessing the 'name' attribute)
print(car1.model)  # Output: R8 (accessing the 'model' attribute)
```

---

## **Self** Keyword

The `self` keyword in Python is used inside a class to refer to the **current instance** of the class. It allows each object to access its own attributes and methods.

### Why do we use `self`?

1. **To refer to object attributes and methods**: Without `self`, Python wouldn't know which object you're referring to, as you could have multiple objects of the same class.
   
2. **To allow each object to have its own unique data**: `self` makes sure that each object can maintain its own set of attributes.

### **For example**:

```python
class Car:
    def __init__(self, brand, model):
        self.name = brand  # Assigning brand to the 'name' attribute
        self.model = model  # Assigning model to the 'model' attribute

    def drive(self):
        print(f"The {self.name} {self.model} is driving!")  # 'self' refers to the current object

car1 = Car("Audi", "R8")  # Creating car1 object
car2 = Car("BMW", "i8")   # Creating car2 object

car1.drive()  # The Audi R8 is driving!
car2.drive()  # The BMW i8 is driving!
```

In this example:
- `self.name` refers to the **name attribute** of the current object.
- When we call `car1.drive()`, the `self` inside the `drive` method refers to `car1`. So `self.name` will access the `name` attribute of `car1` (which is "Audi").
- Similarly, when we call `car2.drive()`, `self` will refer to `car2`.

---

## **Why is `self` needed?**

Without the `self` keyword:
- Python wouldn't know which **object** you're talking about.
- It makes it clear that we're accessing **attributes** and **methods** specific to each object.
  
### Example without `self` (this will not work):

```python
class Car:
    def __init__(self, brand, model):
        name = brand  # Incorrect: this doesn't associate with the current object
        model = model  # Incorrect: this doesn't associate with the current object

    def drive(self):
        print(f"The {name} {model} is driving!")  # Error: name and model are undefined

car1 = Car("Audi", "R8")
car1.drive()  # This will cause an error!
```
In this case, without `self`, the attributes `name` and `model` are **not** tied to the object, and you’ll get an error.

---

## Conclusion

- **Class**: A blueprint to create objects.
- **Constructor**: Initializes the attributes when an object is created.
- **Attributes**: Data associated with an object (e.g., `name`, `model`).
- **`self`**: Refers to the current object and allows access to its attributes and methods.

OOP helps keep code **organized**, **modular**, and **reusable** by grouping related data and actions together. You can easily create multiple o