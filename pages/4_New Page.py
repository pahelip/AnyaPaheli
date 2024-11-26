import google.generativeai as genai
import os
import streamlit as st
import random

key = st.secrets["key"]
genai.configure(api_key = key)


breedData = {
    "Bluetick Coonhound": {"size":"Medium"},
    "African Hunting Dog": {"size":"Medium"}, 
    "Australian Cattle Dog": {"size":"Medium"}, 
    "Kooikerhondje": {"size":"Medium"}, 
    "Saint Bernard": {"size":"Large"}, 
    "Mastiff": {"size":"Large"}, 
    "Bearded Collie": {"size":"Medium"}, 
    "Irish Terrier": {"size":"Small"}, 
    "Pomeranian": {"size":"Small"}, 
    "Finnish Spitz": {"size":"Small"}

}

size = {"Small": 1, "Medium": 2, "Large":3}

first = st.text_input("Enter your first dog breed:")
second = st.text_input("Enter your second dog breed:")

if st.button("Random dog"):
    random_breed = random.choices(["Bluetick Coonhound", "African Hunting Dog", "Australian Cattle Dog", "Kooikerhondje", "Saint Bernard", "Mastiff", "Bearded Collie", "Irish Terrier", "Pomeranian", "Finnish Spitz"])
if first and second:
    if first in breedData and second in breedData:
        one = breedData[first]
        two = breedData[second]
        sizeOne = size[one["size"]]
        sizeTwo = size[two["size"]]
        if sizeOne > sizeTwo:
            winner = one
        elif sizeTwo > sizeOne:
            winner = two
        else:
            winner = None
        st.write("Results:")
        if winner:
            st.write(f"{winner} is larger in size.")
        else:
            st.write(f"Both {one} and {two} are equal in size")

    else:
        st.error("Results are not available for these breeds.")
        

model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
response = model.generate_content("Write a story about these two dog breeds.") #enter your prompt here!
print(response.text) #dont forget to print your response!