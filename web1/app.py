import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load the machine learning model
def load_model():
    with open(r'C:\Users\mohameds\OneDrive\Documents\GitHub\MAIN_CV_PROJECTS\web1\classifier.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Title of the app
st.title("Diabetes Prediction")

# Input fields for user
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, step=1)
glucose = st.number_input('Glucose', min_value=0, max_value=200)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=140)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100)
insulin = st.number_input('Insulin', min_value=0, max_value=900)
bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, format="%.1f")
diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, format="%.3f")
age = st.number_input('Age', min_value=0, max_value=120)

# Prediction button
if st.button('Predict'):
    # Collect the inputs in a numpy array
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, 
                            bmi, diabetes_pedigree_function, age]])
    
    # Make predictions
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f"Predicted Outcome: {'Diabetic' if prediction[0] == 1 else 'Not Diabetic'}")