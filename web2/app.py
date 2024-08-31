import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Set the title of the application
st.set_page_config(page_title="YouTube Spam Detection", layout="wide")

# Create a sidebar for navigation
page = st.sidebar.selectbox("Choose a page", ["Predict", "Explore"])

# Show the selected page
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
