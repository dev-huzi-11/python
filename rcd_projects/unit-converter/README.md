# Unit Converter App

A simple **Unit Converter** built with **Python**, **uv**, and **Streamlit**. This app allows users to convert various units, including length, weight, temperature, volume, and time.

## 🚀 Features
- Convert between multiple units:
  - **Length** (meter, kilometer, inch, foot)
  - **Weight** (gram, kilogram, pound)
  - **Temperature** (Celsius, Fahrenheit, Kelvin)
  - **Volume** (liter, milliliter)
  - **Time** (seconds, minutes, hours)
- User-friendly interface powered by **Streamlit**
- Fast and accurate conversions

🌍 Live Demo

🔗 Try it here: [Unit Converter App](https://unit-converter-w97xndvhwsevgh6sapzy87.streamlit.app/)


## 🛠️ Installation & Setup

### Prerequisites
- **Python** (Ensure you have Python installed)
- **uv** (A modern Python package manager)

### Step 1: Create a Project Folder & Initialize `uv`
```bash
mkdir unit-converter-app
cd unit-converter-app
uv init unit-converter-app
cd unit-converter-app
```

### Step 2: Activate the Virtual Environment
```bash
uv venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate      # On Windows
```

### Step 3: Install Streamlit
Using `uv` package manager:
```bash
uv add streamlit
```

### Step 4: Run the App
```bash
streamlit run app.py
```

This will launch the app in your default web browser.

## 🖥️ Deployment
You can deploy your app on **Streamlit Cloud**:
1. Push your code to **GitHub**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository.
4. Deploy the app.

---
💡 **Contributions & Issues:** Found a bug or want to add a feature? Feel free to open an issue or submit a pull request! 🚀