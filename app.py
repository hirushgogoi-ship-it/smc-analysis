import streamlit as st
import google.generativeai as genai

st.title("🚀 SMC Trading Assistant")
api_key = st.text_input("Apni Gemini API Key daalein:", type="password")
input_data = st.text_area("Apna Market Setup likhein:")

if st.button("Analyze"):
    if api_key and input_data:
        try:
            genai.configure(api_key=api_key)
            genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"SMC trader ke hisaab se analyze karein: {input_data}")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.write("API Key aur Setup dono bharein!")
