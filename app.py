import streamlit as st
import pandas as pd
import joblib


model = joblib.load("your_trained_model.pkl")


st.title("Customer Churn Prediction")
age = st.slider("Age", 18, 100, 30)
subscription_length = st.slider("Subscription Length (Months)", 1, 36, 12)
monthly_bill = st.number_input("Monthly Bill ($)", 1.0, 1000.0, 50.0)
total_usage_gb = st.number_input("Total Usage (GB)", 1.0, 1000.0, 100.0)
gender = st.selectbox("Gender", ["Male", "Female"])

gender_mapping = {"Male": 0, "Female": 1}
gender = gender_mapping.get(gender, 0)

if st.button("Predict Churn"):
    user_data = pd.DataFrame({
        "Age": [age],
        "Subscription_Length_Months": [subscription_length],
        "Monthly_Bill": [monthly_bill],
        "Total_Usage_GB": [total_usage_gb],
        "Gender": [gender]
    })

    prediction = model.predict(user_data)

    if prediction[0] == 0:
        st.success("No Churn (Churn Probability: Low)")
    else:
        st.error("Churn (Churn Probability: High)")
