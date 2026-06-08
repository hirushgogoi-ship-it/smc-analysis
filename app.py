       import streamlit as st
import google.generativeai as genai

st.title("🚀 SMC Trading Assistant")

api_key = st.text_input("Apni Gemini API Key daalein:", type="password")
input_data = st.text_input("Apna Market Setup likhein:")

if st.button("Analyze"):
    if api_key and input_data:
        try:
            genai.configure(api_key=api_key)
            
            
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(input_data)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error details: {e}")
    else:
        st.warning("Please API Key aur Setup dono bharein!")
        

        
