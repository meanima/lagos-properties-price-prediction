import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("house_price_model.pkl")

st.title("Lagos Property Price Prediction App")
st.write("This app predicts the price of a property in Lagos based on its features.")
st.write("Please enter the details of the property below to get an estimated price:")

property_type = st.selectbox(
  "Property Type", [
    'Mini Flat',
    'Self Contain / Shared Room',
    'Terraced Duplex',
    'Luxury Apartment',
    'Detached / Semi-Detached Duplex',
    'Standard Flat / Apartment',
    'Commercial Property',
    'Land'
  ]
)

location = st.selectbox(
  "Location", [
    "Abule Egba", "Agege", "Ajah", "Alimosho", "Amuwo Odofin", "Apapa", "Bariga", "Egbe Idimu", "Ejigbo", "Epe", "Gbagada", "Ibeju Lekki", "Iju", "Ikeja", "Ikorodu", "Ikotun Igando", "Ikoyi", "Ilupeju", "Ipaja", "Isolo", "Ketu", "Kosofe Ikosi", "Lagos Island", "Lekki", "Maryland", "Mushin", "Ogba", "Ogudu", "Ojo", "Ojodu", "Ojota", "Okota", "Oshodi", "Sangotedo", "Shomolu", "Surulere", "Victoria Island", "Yaba"
  ]
)

bedrooms = st.slider('No. of Bedrooms', 0, 10, 1)
bathrooms = st.slider('No. of Bathrooms', 0, 10, 1)

if st.button("Predict Price"):
  input_data = pd.DataFrame(
    {
      'Property Type': [property_type],
      'Location': [location],
      'Bedrooms': [bedrooms],
      'Bathrooms': [bathrooms]
    }
  )

  prediction = model.predict(input_data)

  if prediction[0] <= 5_000_000:
        category = "Budget 🟢"
  elif prediction[0] > 5_000_000 and prediction[0] <= 20_000_000:
      category = "Mid-Range 🟡"
  else:
      category = "Luxury 🔴"

  st.success(f"The estimated price of the property is: ₦{prediction[0]:,.2f}")
  st.info(f"Price Category: {category}")