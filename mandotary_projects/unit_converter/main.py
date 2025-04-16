import streamlit as st
from unit_converter import unit_conversion

unit_categories = {
    "weight": ["gram", "kilogram", "pound", "ounce"],
    "temperature": ["celsius", "kelvin", "fahrenheit"],
    "time": ["second", "minute", "hour", "day", "week"],
    "volume": ["liter", "milliliter", "gallon", "cubic_meter", "cup"],
    "length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "foot", "inch"]
}

st.title("🧮 Unit Converter")

value = st.number_input("Enter the value", min_value=1.0, step=1.0)

select_category = st.radio("Select Category", list(unit_categories.keys()), horizontal=True)

units = unit_categories[select_category]

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("Convert from:", options=units)

with col2:
    to_unit = st.selectbox("Convert to:", options=units)

if st.button("Convert"):
    result = unit_conversion(value=value, from_unit=from_unit, to_unit=to_unit)

    if isinstance(result, str): 
        st.write(result)  
    else:
        st.success(f"✅ Converted value: {result:.2f} {to_unit}")
