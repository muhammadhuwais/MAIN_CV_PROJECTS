import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Set page configuration
st.set_page_config(page_title="Sonar Rock/Mine Prediction", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Predict", "Explore"])

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
