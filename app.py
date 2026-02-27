import streamlit as st
from openai import OpenAI

st.title("Test OpenAI + Streamlit")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if st.button("Test connessione"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Scrivi solo: Connessione OK"}
        ]
    )
    st.write(response.choices[0].message.content)
