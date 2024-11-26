import requests

API_URL = "https://api.thedogapi.com/v1/images/search"
API_KEY = "live_bvXwtUCuseTj0LLHnlsUcvprBx0d0tn43fChCbza0AJ9DYnR4Xb6TYRuDRXKd4RE"

def fetch_dog_data(limit = 1):
    params = {"limit": limit,"api_key": API_KEY}
    response = requests.get(API_URL, params=params)
    return response.json()


import streamlit as st

dog_data = fetch_dog_data()

st.header("**Dog of the Day**")

num = st.slider("Number of dogs:", min_value =  1, max_value = 10, value = 1)

if "dog_data" not in st.session_state: #NEW
    st.session_state["dog_data"] = fetch_dog_data(limit = num)



dog_data = st.session_state["dog_data"]
info_choice = st.radio("Select the information you want to see!", ["Breed", "Size", "Temperament"])

for dogType in dog_data:
    st.image(dogType["url"], caption="Dog of the Day")
    if "breeds" in dogType and dogType["breeds"]:
        if info_choice == "Breed":
            st.write("Breed: ", dogType["breeds"][0]["name"])   
        elif info_choice == "Size":
            st.write("Size: ", dogType["breeds"][0]["weight"]["imperial"])  
        elif info_choice == "Temperament":
            st.write("Temperament: ", dogType["breeds"][0]["temperament"])
    else:
        st.error("Could not fetch data. Try again later.") #NEW

if st.button("Go"): #NEW
    st.session_state["dog_data"] = fetch_dog_data(limit = num)

   
        

