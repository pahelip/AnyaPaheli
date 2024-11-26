import requests

API_URL = "https://api.thedogapi.com/v1/images/search"
API_KEY = "live_bvXwtUCuseTj0LLHnlsUcvprBx0d0tn43fChCbza0AJ9DYnR4Xb6TYRuDRXKd4RE"

def fetch_dog_data(limit = 1):
    params = {"limit": 1,"api_key": API_KEY}
    response = requests.get(API_URL, params=params)
    return response.json()[0]


import streamlit as st

dog_data = fetch_dog_data()

st.header("**Dog of the Day**")

num = st.slider("Number of dogs:", min_value =  1, max_value = 10, value = 1)

if "dog_data" not in st.session_state: #NEW
    st.session_state["dog_data"] = fetch_dog_data()

dog_data = st.session_state["dog_data"]
st.image(dog_data["url"], caption="Dog of the Day")

if st.button("Fetch New Dog"): #NEW
    numDogs = fetch_dog_data(limit = num)
    st.session_state["dog_data"] = fetch_dog_data()

info_choice = st.radio("Select the information you want to see!", ["Breed", "Size", "Temperament"])

if info_choice == "Breed":
    if dog_data["breeds"]:
        st.write("Breed: ", dog_data["breeds"][0]["name"])
    else:
        st.write("We aren't sure... But if you see this dog, be sure to ask!")
elif info_choice == "Size":
    if dog_data["breeds"]:
        st.write("Size: ", dog_data["breeds"][0]["weight"]["imperial"])
    else:
        st.write("Depends on the dog! Can be small, big, or giant!")
elif info_choice == "Temperament":
    if dog_data["breeds"]:
        st.write("Temperament: ", dog_data["breeds"][0]["temperament"])
    else:
        st.write("Depends on the day! The dog can be playful or moody...")
else:
    st.error("Could not fetch data. Try again later.") #NEW
