# Simple Chatbot

This is a simple chatbot built using Python, `uv`, and `chainlit`. The chatbot takes user input and responds with:

> **You said:** `<your question>`

## Features
- Accepts user input
- Echoes the message with a predefined response
- Uses `uv` for dependency management
- Uses `chainlit` for creating the chatbot interface

## Installation

Make sure you have Python installed on your system.

1. Create a new folder for your project:
   ```sh
   mkdir simple-chatbot
   cd simple-chatbot
   ```

2. Initialize the project with `uv`:
   ```sh
   uv init simple-chatbot
   ```

3. Move into the newly created project folder:
   ```sh
   cd simple-chatbot
   ```

4. Install `chainlit` using `uv`:
   ```sh
   uv add chainlit
   ```

5. Activate the environment:
   - For Windows (Command Prompt/PowerShell):
     ```sh
     .venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```

## Usage

Run the chatbot using:
```sh
chainlit run main.py
```

Then, open the provided local server URL in your browser and start chatting!

## Example Interaction
**User:** Hello, how are you?

**Chatbot:** You said: Hello, how are you?

## Dependencies
- Python 3.x
- `uv` (for package management)
- `chainlit`

---