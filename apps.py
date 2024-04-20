import streamlit as st
import pandas as pd
import pickle
from joblib import load

model = load('Diabetes_Prediction_model.pkl')


# Set page config to add a logo and set a wide page layout
st.set_page_config(page_title="Diabetes Prediction Model", page_icon=":hospital:", layout="wide")

# Title and introduction text
#st.image("path/to/your/logo_or_image.png", width=100)  # Add your logo
st.title('Diabetes Prediction Model')
st.write("This tool predicts the likelihood of diabetes based on patient information.")

# Sidebar for user input
with st.sidebar:
    st.header('Patient Data Input')
    age = st.number_input('Age', min_value=0.0, max_value=120.0, step=0.1, format="%.1f")
    bmi = st.number_input('Body Mass Index (BMI)', min_value=0.0, step=0.1, format="%.1f")
    hbA1c_level = st.number_input('HbA1c Level', min_value=0.0, step=0.1, format="%.1f")
    blood_glucose_level = st.number_input('Blood Glucose Level', min_value=0.0, step=1.0)
    gender_male = st.selectbox('Gender', [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    hypertension_1 = st.selectbox('Hypertension', [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    heart_disease_1 = st.selectbox('Heart Disease', [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    smoking_history_trans_past = st.selectbox('Smoking History - Past', [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    smoking_history_trans_present = st.selectbox('Smoking History - Present', [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

# Main page for model output
st.header('Prediction Output')
if st.sidebar.button('Predict'):
    input_data = pd.DataFrame([[age, bmi, hbA1c_level, blood_glucose_level,
                                gender_male, hypertension_1, heart_disease_1,
                                smoking_history_trans_past, smoking_history_trans_present]],
                              columns=['age', 'bmi', 'HbA1c_level', 'blood_glucose_level',
                                       'gender_Male', 'hypertension_1', 'heart_disease_1',
                                       'smoking_history_trans_past', 'smoking_history_trans_present'])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    

    if prediction == 1:
        st.error('The model predicts the patient is diabetic.')
        st.markdown("### Helpful Resources")
        st.markdown("[Learn more about managing diabetes](https://www.diabetes.org)")
    else:
        st.success('The model predicts the patient is not diabetic.')
        st.markdown("### Helpful Resources")
        st.markdown("[Learn more about managing diabetes](https://www.diabetes.org)")
