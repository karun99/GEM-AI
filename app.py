import streamlit as st
from google_generativeai import GenerativeModel

# Replace 'YOUR_API_KEY' with your actual Gemini API key
API_KEY = "YOUR_API_KEY"

st.title("Gemini Chatbot")

# Initialize GenerativeModel with the 'gemini-pro' model
model = GenerativeModel(model="gemini-pro", api_key=API_KEY)

chat_history = []

def generate_response(user_input):
  if user_input.strip() == "":
    return "Please enter a message."

  # Create a Content object representing the user's message
  prompt = [Content.text(user_input)]

  try:
    # Generate a response from the Gemini API
    response = model.generate_content(prompt)
    chat_history.append({"sender": "User", "text": user_input})
    chat_history.append({"sender": "Gemini", "text": response.text})
    return response.text
  except Exception as e:
    # Handle potential errors gracefully
    print(f"Error generating response: {e}")
    return "An error occurred. Please try again later."

user_input = st.text_input("Enter your message:")

if user_input:
  response = generate_response(user_input)
  st.write(response)

  # Display chat history
  for message in chat_history:
    st.write(f"{message['sender']}: {message['text']}")
