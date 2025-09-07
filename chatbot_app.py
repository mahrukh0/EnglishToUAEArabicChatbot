import streamlit as st
from googletrans import Translator

# Initialize translator
translator = Translator()

# UAE Arabic dictionary for common phrases
uae_dict = {
    "hello": "هلا",
    "hi": "هلا",
    "how are you?": "شلونك؟",
    "thank you": "مشكور",
    "thanks": "مشكور",
    "yes": "إيه",
    "no": "لا",
    "please": "لو سمحت",
    "goodbye": "مع السلامة"
}

# Function to apply UAE dialect replacements
def apply_uae_dialect(text):
    lower_text = text.lower()
    for key, value in uae_dict.items():
        if key in lower_text:
            text = text.replace(key, value)
    return text

# Streamlit UI
st.title("English → UAE Arabic Chatbot")

user_input = st.text_input("Type your message in English:")

if user_input:
    # Translate with Google
    translated_text = translator.translate(user_input, src='en', dest='ar').text
    # Apply UAE dialect adjustments
    translated_text = apply_uae_dialect(translated_text)
    st.write("💬 UAE Arabic Translation:")
    st.write(translated_text)
