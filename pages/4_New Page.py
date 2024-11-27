import random
import google.generativeai as genai
import os
import streamlit as st


key = st.secrets["key"]
genai.configure(api_key = key)

"""
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
    first,second = random.sample(list(breedData.keys()),2)
    st.write(f"The randomly selected dogs are: {first}, {second}")
if first and second:
    if first in breedData and second in breedData:
        one = breedData[first]
        two = breedData[second]
        sizeOne = size[one["size"]]
        sizeTwo = size[two["size"]]
        if sizeOne > sizeTwo:
            winner = first
        elif sizeTwo > sizeOne:
            winner = second
        else:
            winner = None
        st.write("Results:")
        if winner:
            st.write(f"{winner} is larger in size.")
        else:
            st.write(f"Both {first} and {second} are equal in size!")

    else:
        st.error("Results are not available for these breeds.")


model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
response = model.generate_content("Write a story about these two dog breeds.") #enter your prompt here!
print(response.text) #dont forget to print your response!
"""

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

st.write(generate(f"{comparison_data}\n\n\Provide a detailed comparison of these two breeds."))

