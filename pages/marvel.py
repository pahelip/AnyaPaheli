import requests

API_URL = "https://api.thedogapi.com/v1/images/search"
API_KEY = "live_bvXwtUCuseTj0LLHnlsUcvprBx0d0tn43fChCbza0AJ9DYnR4Xb6TYRuDRXKd4RE"

def fetch_dog_data():
    params = {"limit": 1,"api_key": API_KEY}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None


import streamlit as st

dog_data = fetch_dog_data()

if dog_data:
    st.image(dog_data["url"], caption="Dog of the Day", use_column_width=True)

    if st.button("Fetch New Dog"):
        st.experimental_rerun()

    info_choice = st.radio("Select the type of information to display:", ["Breed", "Size", "Temperament"])

    if info_choice == "Breed":
        st.write("Breed: ", dog_data["breeds"][0]["name"] if dog_data["breeds"] else "Unknown")
    elif info_choice == "Size":
        st.write("Size: ", dog_data["breeds"][0]["weight"]["metric"] if dog_data["breeds"] else "Unknown")
    elif info_choice == "Temperament":
        st.write("Temperament: ", dog_data["breeds"][0]["temperament"] if dog_data["breeds"] else "Unknown")
else:
    st.error("Could not fetch data. Try again later.")