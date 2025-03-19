# ******************************************* GREETING *******************************************

# Function to generate a greeting message
# It has a default parameter 'user' set to "user" in case no name is provided
def greeting(user = "user"):
    return f"Hi {user}! Welcome to our company"  # Returns a formatted greeting message

# Calling the function with a specific name
print(greeting("Huzaifa"))  # Output: Hi Huzaifa! Welcome to our company

# Calling the function without an argument (uses the default value "user")
print(greeting())  # Output: Hi user! Welcome to our company