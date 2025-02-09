import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle 

# load pickle file
with open('house_price_predictor.pkl', 'rb') as f:
    dit = pickle.load(f)

b1,head,b2 = st.columns([0.15,0.7,0.15],vertical_alignment="bottom")
head.title("House Price Prediction")

# get user input
with st.form("HP", True):
    bedrooms = st.number_input("Number of Bedrooms:",0,8)

    bathrooms = st.number_input("Number of Bathrooms:",0,6)

    sqft = st.number_input("House SquareFeet:",300,8000)

    floors = st.number_input("House Floors:",0,3)

    waterfront = st.selectbox("House Waterfront:",["No","Yes"])
    if waterfront == "Yes":
        waterfront = 1
    else:
        waterfront = 0

    view = st.slider("House View:",0,4)

    grade = st.slider("House Look Grade:",1,13)

    year = st.number_input("Year Built:",1900,2015)

    renovated = st.selectbox("House Renovated?",["No","Yes"])
    if renovated == "Yes":
        renovated = 1
    else:
        renovated = 0

    zipcode = st.selectbox("Zip Code:",dit["Zip"])

    submit_button = st.form_submit_button("Submit")

    # make prediction
    if submit_button:
        features = np.array([[bedrooms, bathrooms, sqft, floors, waterfront, view, grade, year, renovated]])
        zip = dit["OneHot"].transform([[zipcode]])
        arr = np.hstack([features, zip])

        pred = round(dit["Model"].predict(arr)[0])

        st.text_input("Predicted House Price:",value= f"₹{pred}",disabled=True)
