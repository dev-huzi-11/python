# Importing the Streamlit library for creating a web app
import streamlit as stream

# Function to perform unit conversion
def unit_conversion(value, from_unit, to_unit):
    """Unit converter function"""

    # Dictionary containing conversion factors
    conversions = {
        # Length conversion
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometers
        "kilometer_meter": 1000,   # 1 kilometer = 1000 meters
        "foot_inches": 12,         # 1 foot = 12 inches
        "inches_foot": 1/12,       # 1 inch = 1/12 foot

        # Weight conversion
        "gram_kilogram": 0.001,    # 1 gram = 0.001 kilograms
        "kilogram_gram": 1000,     # 1 kilogram = 1000 grams
        "gram_pound": 0.00220462,  # 1 gram ≈ 0.00220462 pounds
        "pound_gram": 453.592,     # 1 pound ≈ 453.592 grams
        "kilogram_pound": 2.20462, # 1 kilogram ≈ 2.20462 pounds
        "pound_kilogram": 0.453592,# 1 pound ≈ 0.453592 kg

        # Volume conversion
        "milliliter_liter": 0.001,  # 1 milliliter = 0.001 liter
        "liter_milliliter": 1000,   # 1 liter = 1000 milliliters

        # Time conversion
        "minute_second": 60,       # 1 minute = 60 seconds
        "second_minute": 1/60,     # 1 second = 1/60 minute
        "minute_hour": 1/60,       # 1 minute = 1/60 hour
        "hour_minute": 60,         # 1 hour = 60 minutes
    }

    # Temperature conversion logic (not included in dictionary since formulas are required)
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32  # Celsius to Fahrenheit
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9  # Fahrenheit to Celsius
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15  # Celsius to Kelvin
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15  # Kelvin to Celsius

    # Creating a key to match the conversion direction
    key = f"{from_unit}_{to_unit}"

    # Checking if the conversion is available in the dictionary
    if key in conversions:
        conversion = conversions[key]  # Getting the conversion factor
        return value * conversion  # Converting and returning the result
    else:
        return "Conversion not supported"  # Message if conversion is not available

# Setting the title of the Streamlit web app
stream.title("Unit Converter")

# Creating a number input field for the user to enter a value
value = stream.number_input("Enter the value", min_value=1.0, step=1.0)

# Dropdown menu for selecting the unit to convert from
from_unit = stream.selectbox(
    "Convert from: ",
    [
        # Length units
        "meter", "kilometer", "foot", "inches",
        
        # Weight units
        "gram", "kilogram", "pound",
        
        # Volume units
        "milliliter", "liter",
        
        # Time units
        "second", "minute", "hour",
        
        # Temperature units
        "celsius", "fahrenheit", "kelvin"
    ]
)

# Dropdown menu for selecting the unit to convert to
to_unit = stream.selectbox(
    "Convert to: ",
    [
        # Length units
        "meter", "kilometer", "foot", "inches",
        
        # Weight units
        "gram", "kilogram", "pound",
        
        # Volume units
        "milliliter", "liter",
        
        # Time units
        "second", "minute", "hour",
        
        # Temperature units
        "celsius", "fahrenheit", "kelvin"
    ]
)

# Button to trigger the conversion
if stream.button("Convert"):
    result = unit_conversion(value, from_unit, to_unit)  # Calling the conversion function
    
    if isinstance(result, str):  # If the function returns an error message
        stream.write(result)  # Display the message as it is
    else:
        stream.write(f"Converted value: {result:.2f}")  # Format the result properly
