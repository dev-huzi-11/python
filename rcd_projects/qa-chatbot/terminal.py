import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:
    user_input = input("Enter your question or(quit to exist): ")

    if user_input.lower() == "quit":
        print("Thanks for chatting. Goodbye!")
        break

    response = model.generate_content(user_input)


    print(response.text)