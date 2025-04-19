# 🔐 Password Strength Checker

A Streamlit-based web app that helps users evaluate the strength of their passwords and generate secure ones with customizable length.

## 🌐 Live App

👉 [Click here to try the Password Strength Checker](https://huzi-strengthchecker-evsp4v5ds3qedrnpnemsm2.streamlit.app/)

## 💡 Features

- ✅ **Password Strength Evaluation**
  - Checks password against common weaknesses:
    - Minimum length
    - Presence of uppercase & lowercase
    - At least one digit
    - At least one special character
    - Avoids blacklisted (commonly used) passwords
  - Feedback provided with appropriate strength level:
    - Strong
    - Moderate
    - Weak
    - Common (blacklisted)

- 🔐 **Secure Password Generator**
  - Optional toggle to generate a strong password
  - Adjustable length using a slider
  - Password meets all security criteria:
    - Includes lowercase, uppercase, digits, and symbols
    - Randomized and shuffled for maximum security

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/) — for building the UI
- Python — logic for password validation and generation
- Regular Expressions — for checking character rules

## 🎯 Goal

Empower users with an easy-to-use tool for:
- Validating password security
- Learning what makes a strong password
- Instantly generating secure passwords

---