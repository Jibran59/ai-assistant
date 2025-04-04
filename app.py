import streamlit as st
import openai  

# OpenAI API Key (Isko GitHub Secrets me rakhna better hai)
OPENAI_API_KEY = "yahan_apni_api_key_dalo"

# Streamlit UI
st.title("🤖 AI Assistant - YouTube, Story & Study Helper")
st.write("Apna GPT Assistant - Hindi-English Style mein")

# Task Selection
task = st.selectbox("Task choose karo:", ["YouTube Script", "Story", "Study Help"])

# User Input
user_input = st.text_area("Apna topic ya idea yahan likho:")

if st.button("Generate"):
    if OPENAI_API_KEY:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7
        )
        st.write(response["choices"][0]["message"]["content"])
    else:
        st.error("⚠️ API key missing! Please add your OpenAI API key.")