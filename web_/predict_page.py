import streamlit as st
import numpy as np
import pickle

# Load the model
def load_model():
    with open(r'C:\Users\mohameds\OneDrive\Documents\GitHub\MAIN_CV_PROJECTS\web_\logisticregression.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

def show_predict_page():
    st.title("Sonar Rock/Mine Prediction")

    st.write("""### Enter the values for the 60 features:""")
    
    # Create input fields for all features
    inputs = []
    for i in range(60):  # Sonar dataset has 60 features
        value = st.number_input(f"Feature {i+1}", min_value=0.0, max_value=1.0, step=0.01)
        inputs.append(value)
    
    input_data = np.asarray(inputs).reshape(1, -1)
    
    if st.button("Predict"):
        prediction = model.predict(input_data)
        if prediction[0] == 'R':  # Assuming 'R' is for Rock
            st.write("The object is a **Rock**")
        else:
            st.write("The object is a **Mine**")
