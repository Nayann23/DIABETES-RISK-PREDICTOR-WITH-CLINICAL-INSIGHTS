import streamlit as st
import pickle
import pandas as pd
from scipy.sparse import hstack
import numpy as np

# Load pickled objects
with open("rf_model.pkl", "rb") as f:
    rf_model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

st.title("Diabetes Prediction App")

# User input for key numeric features
age = st.number_input("Age", min_value=0, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
glucose = st.number_input("Glucose Level", min_value=0.0, max_value=500.0, value=100.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=80.0)
insulin = st.number_input("Insulin Level", min_value=0.0, max_value=1000.0, value=100.0)

# Clinical notes input
clinical_notes = st.text_area("Clinical Notes")

if st.button("Predict"):
    # Create numeric input with all features expected by the scaler
    # Fill unused features with default values (e.g., 0 or median from training)
    numeric_input = np.zeros(len(scaler.scale_))  # scaler.scale_ gives the number of features used during training

    # Assign values for the selected features (adjust indices to match your training dataset)
    numeric_input[0] = age
    numeric_input[1] = bmi
    numeric_input[2] = glucose
    numeric_input[3] = blood_pressure
    numeric_input[4] = insulin
    # The rest of numeric_input remains 0

    numeric_input = numeric_input.reshape(1, -1)
    numeric_scaled = scaler.transform(numeric_input)

    # TF-IDF for clinical notes
    text_tfidf = tfidf.transform([clinical_notes])

    # Combine numeric and text features
    final_input = hstack([numeric_scaled, text_tfidf])

    # Predict
    prediction = rf_model.predict(final_input)[0]
    prediction_proba = rf_model.predict_proba(final_input)[0][1]

    st.write("**Prediction:**", "Diabetes" if prediction == 1 else "No Diabetes")
    st.write("**Prediction Probability (Diabetes):**", round(prediction_proba, 2))
