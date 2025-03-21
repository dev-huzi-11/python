# *************************** FUNCTION WITH KWARGS ***************************

# Defining a function that accepts keyword arguments (**kwargs)
def kwargs(**kwargs):  
    # Looping through the keyword arguments and printing their key-value pairs
    for key, value in kwargs.items():  
        print(f"{key}: {value}")  # Printing key-value pairs in a formatted way


# Calling the function with different keyword arguments
kwargs(name="Huzaifa", age=17)  
kwargs(name="Ahsan", age=18, isMarried=False)