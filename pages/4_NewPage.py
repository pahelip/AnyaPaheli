import google.generativeai as genai
import os
import streamlit as st

key = st.secrets["key"]
genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
response = model.generate_content("Write a poem about dogs!") #enter your prompt here!
print(response.text) #dont forget to print your response!
