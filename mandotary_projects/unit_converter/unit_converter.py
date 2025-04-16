from typing import Union

def unit_conversion(value: float, from_unit: str, to_unit: str) -> Union[str, float]:
    """Unit Converter function"""

    conversions = {
        # Length conversion
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "meter_centimeter": 100,
        "centimeter_meter": 0.01,
        "meter_millimeter": 1000,
        "millimeter_meter": 0.001,
        "mile_kilometer": 1.60934,
        "kilometer_mile": 1/1.60934,
        "foot_meter": 0.3048,
        "meter_foot": 3.28084,
        "inch_meter": 0.0254,
        "meter_inch": 39.3701,

        # Weight conversion
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "gram_pound": 0.00220462,
        "pound_gram": 453.592,
        "kilogram_pound": 2.20462,
        "pound_kilogram": 0.453592,
        "ounce_gram": 28.3495,
        "gram_ounce": 0.035274,

        # Volume conversion
        "milliliter_liter": 0.001,
        "liter_milliliter": 1000,
        "liter_gallon": 0.264172,
        "gallon_liter": 3.78541,
        "liter_cubic_meter": 0.001,
        "cubic_meter_liter": 1000,
        "cup_liter": 0.236588,
        "liter_cup": 4.22675,

        # Time conversion
        "second_minute": 1/60,
        "minute_second": 60,
        "minute_hour": 1/60,
        "hour_minute": 60,
        "second_hour": 1/3600,
        "hour_second": 3600,
        "day_hour": 24,
        "hour_day": 1/24,
        "day_second": 86400,
        "second_day": 1/86400,
        "week_day": 7,
        "day_week": 1/7,
    }

    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32  # Celsius to Fahrenheit
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9  # Fahrenheit to Celsius
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15  # Celsius to Kelvin
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15  # Kelvin to Celsius
    
    key = f"{from_unit}_{to_unit}"

    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not possible"