import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

st.title("Pregnancy Risk Level Predictor")

input_data = []
for feature in features:
    value = st.number_input(f"Enter {feature}", step=1.0)
    input_data.append(value)

if st.button("Predict"):
    result = model.predict([input_data])[0]
    if result == 1:
        st.warning("⚠️ High Risk Pregnancy")
    else:
        st.success("✅ Low Risk Pregnancy")
