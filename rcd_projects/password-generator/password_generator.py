import streamlit as st
import random
import string

def password_generator(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds 0-9

    if use_special:
        characters += string.punctuation  # Adds special characters (!@#$...)

    return "".join(random.choice(characters) for _ in range(length))  # Generates password

# Streamlit UI
st.title("🔐 Password Generator")

# Initialize session state for the password
if "password" not in st.session_state:
    st.session_state.password = ""

length = st.slider("Select password length", min_value=8, max_value=32, value=12)

use_digits = st.checkbox("Include numbers")
use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    st.session_state.password = password_generator(length, use_digits, use_special)

# Display the generated password
if st.session_state.password:
    st.write("Generated Password:")
    st.code(st.session_state.password)  # Display the password in a code block for easy copying