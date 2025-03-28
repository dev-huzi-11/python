# Chainlit Chatbot with Gemini API

This project is a chatbot powered by **Chainlit** and **Google's Gemini AI (Generative AI)**. It allows users to chat with the Gemini AI in real-time.

---

## 🚀 Features
- Uses **Google Gemini AI** to generate responses.
- Built with **Chainlit** for an interactive chatbot experience.
- Securely loads API keys using **dotenv**.
- Handles API errors gracefully.

---

## 🛠 Installation Guide

Follow these step-by-step instructions to set up and run the chatbot on your local machine.

### **1️⃣ Create a Project Folder**
First, create a folder for your project and navigate into it:
```sh
mkdir qa-chatbot
cd qa-chatbot
```

### **2️⃣ Initialize the Project**
Use `uv` to initialize the project:
```sh
uv init qa-chatbot
```

### **3️⃣ Navigate to the Created Folder**
Move into the newly created folder:
```sh
cd qa-chatbot
```

### **4️⃣ Install Dependencies**
Run the following command to install the required libraries:
```sh
uv add chainlit google-generativeai python-dotenv
```

### **5️⃣ Activate the Virtual Environment**
Activate the virtual environment:
- **Windows:**
  ```sh
  .venv/Scripts/activate
  ```
- **Mac/Linux:**
  ```sh
  source .venv/bin/activate
  ```

### **6️⃣ Set Up Environment Variables**
Create a **.env** file in the root directory of your project and add your Gemini API key:
```sh
GEMINI_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your actual **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/).

### **7️⃣ Run the Terminal Chatbot**
To run the terminal-based chatbot, use:
```sh
uv run terminal.py
```

### **8️⃣ Run the Chainlit Chatbot**
To start the Chainlit chatbot interface, run:
```sh
chainlit run main.py
```

If you see **"Hi, How can I assist you today?"**, your chatbot is working correctly! 🎉

---

## 📌 Usage
- Type your question in the chat.
- The chatbot will respond using **Gemini AI**.
- Type `quit` to exit the chat. (for terminal based chatbot)

---