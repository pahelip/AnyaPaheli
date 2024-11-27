import random
import requests
import google.generativeai as genai
import os
import streamlit as st

key = st.secrets["key"]
genai.configure(api_key = key)

st.header("Hi! I am Dogbot")
st.subheader("I am here to help you find information about different dog breeds. Please enter the relevant information in the boxes below.")

first = st.text_input("Enter your first dog breed:")
second = st.text_input("Enter your second dog breed:")

api_url="https://api.thedogapi.com/v1/breeds"
api_key="live_bvXwtUCuseTj0LLHnlsUcvprBx0d0tn43fChCbza0AJ9DYnR4Xb6TYRuDRXKd4RE"

def getDogData(dogBreed):
    try:
        resp=requests.get(f"{api_url}?api_key={api_key}")

        breeds=resp.json()

        for aBreed in breeds:
            if dogBreed.strip().lower() == aBreed["name"].strip().lower():
                return aBreed

    except:
        st.error("There is no data for this breed! Try a new one")
        return None
  

def format(breed):
    if breed==None:
        return "Breed not found."
    else:
        return (f"Name: {breed['name']}\n"
            f"Temperament: {breed['temperament']}\n"
            f"Life Span: {breed['life_span']}\n"
            f"Weight: {breed['weight']['imperial']} lbs\n"
            f"Height: {breed['height']['imperial']} in")

breed1=getDogData(first)
breed2=getDogData(second)


comparison_data = (f"Compare these two dog breeds:\n\n"
    f"Breed 1:\n{format(breed1)}\n\n"
    f"Breed 2:\n{format(breed2)}")

def generate(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(prompt)
    content = response._result.candidates[0].content.parts[0].text
    return content

st.write(generate(f"{comparison_data}\n\nProvide a detailed comparison of these two breeds."))

st.subheader("Dogbot here to answer anymore questions.")

question = st.text_input("Ask me a question about the dog breeds!")

def chatbot(question):
    if not question.strip():
        return None
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response=model.generate_content(question)
        content=response._result.candidates[0].content.parts[0].text
        return content
    except:
        st.write("Please ask me a question.")
st.write(generate(question))