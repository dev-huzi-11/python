import streamlit as st
import string
import random
import re

# A list of common blacklisted passwords
blacklist = ["password123", "12345678", "password", "admin"]

# Function to check if the password is in the blacklist
def blacklisted_password(password: str) -> bool:
    return password.lower() in blacklist

# Function to check the strength of a password based on multiple criteria
def password_strength_checker(password: str) -> str:
    score = 0
    feedback = []

    # Check if the password is blacklisted
    if blacklisted_password(password):
        return "🚫 This password is too common. Please choose another."

    # Check if password length is at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters.")

    # Check if password contains both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include both uppercase and lowercase.")

    # Check if password contains at least one number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Check if password contains at least one special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*)")

    # Return feedback based on the score
    if score == 4:
        return "✅ Strong Password\n" + "\n".join(feedback)
    elif score == 3:
        return "⚠️ Moderate Password\n" + "\n".join(feedback)
    else:
        return "❌ Password is too weak\n" + "\n".join(feedback)

# Function to suggest a strong password with the given length
def suggest_strong_password(length=12) -> str:
    if length < 8:  # Ensure the password is at least 8 characters long
        length = 8

    # Defining character sets to include lowercase, uppercase, digits, and symbols
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"

    # Start password with at least one lowercase, uppercase, digit, and symbol
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password with random characters from all sets
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to randomize character positions
    random.shuffle(password)
    return ''.join(password)

# Streamlit UI configuration
st.set_page_config(page_title="Password Strength Checker")
st.title("🔐 Password Strength Checker")

# Input field for the user to enter a password
password_input = st.text_input("Enter your password", type="password")

# Button to trigger password strength check
if st.button("Check Password Strength"):
    if password_input:
        result = password_strength_checker(password_input)  # Check password strength

        # Display appropriate result based on password strength
        if "Strong" in result:
            st.success(result)
        elif "Moderate" in result:
            st.warning(result)
        elif "weak" in result:
            st.error(result)
        elif "common" in result:
            st.error(result)
    else:
        st.error("Please enter a password.")

# Logic to suggest a strong password
if "show_slider" not in st.session_state:
    st.session_state.show_slider = False  # Track whether the slider is shown or not

# Button to allow user to opt for a suggested strong password
if not st.session_state.show_slider:
    if st.button("Want to suggest a strong password?"):
        st.session_state.show_slider = True  # Show the slider for password length selection

# Slider for selecting password length and generating a password
if st.session_state.show_slider:
    length = st.slider("🔧 Select password length", min_value=8, max_value=24, value=12)
    if st.button("Generate Password"):
        suggested_password = suggest_strong_password(length)  # Generate strong password
        st.success(f"💡 Suggested Password:\n`{suggested_password}`")