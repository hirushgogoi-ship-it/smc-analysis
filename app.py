import streamlit as st
from openai import OpenAI

st.title("🚀 Trading Assistant (Powered by GPT)")

api_key = st.text_input("Apni OpenAI API Key daalein:", type="password")
input_data = st.text_input("Apna Market Setup likhein:")

if st.button("Analyze"):
    if api_key and input_data:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", # Ya "gpt-4o" agar aapke paas access hai
                messages=[
                    {"role": "system", "content": "You are an expert SMC trading analyst."},
                    {"role": "user", "content": input_data}
                ]
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please API Key aur Setup dono bharein!")



        
