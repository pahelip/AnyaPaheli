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

if st.button("Go"): #NEW
    st.session_state["dog_data"] = fetch_dog_data(limit = num)

if "dog_data" not in st.session_state: #NEW
    st.session_state["dog_data"] = fetch_dog_data(limit = num)


dog_data = st.session_state["dog_data"]

info_choice = st.radio("Select the information you want to see!", ["Breed", "Size", "Temperament"])

dog_labels=[]

for dogType in dog_data:
    st.image(dogType["url"], caption="Dog of the Day", width=250)
    if "breeds" in dogType and dogType["breeds"]:
        breed_name=dogType["breeds"][0]["name"]
        dog_labels.append(breed_name)
        if info_choice == "Breed":
            st.write("Breed: ", dogType["breeds"][0]["name"])
        elif info_choice == "Size":
            st.write("Size: ", dogType["breeds"][0]["weight"]["imperial"])  
        elif info_choice == "Temperament":
            st.write("Temperament: ", dogType["breeds"][0]["temperament"])
    else:
        st.write("No info for this dog... Looks like it is a very mysterious breed.")
        dog_labels.append("Unknown Breed")

st.subheader("**Detailed Information**")

selected_dog = st.selectbox("Choose a dog to learn more:", options=dog_labels) #NEW

if selected_dog=="Unknown Breed":
    st.write("We aren't sure of more information about this dog... If you see one be sure to ask it for us.")
else:
    for dogType in dog_data:
        if "breeds" in dogType and dogType["breeds"]:
            if dogType["breeds"][0]["name"]==selected_dog:
                st.write(f"More information about the {selected_dog}")
                st.write("Breed Group Type: ", dogType["breeds"][0].get("breed_group", "N/A"))
                st.write("Life Span: ", dogType["breeds"][0].get("life_span", "N/A"))
                st.write("Bred For: ", dogType["breeds"][0].get("bred_for", "N/A"))
                st.write("Height: ", dogType["breeds"][0]["height"]["imperial"])
                st.write("Weight: ", dogType["breeds"][0]["weight"]["imperial"])

