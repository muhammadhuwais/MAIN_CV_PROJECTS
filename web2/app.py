import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


import streamlit as st

# Set page configuration first
st.set_page_config(page_title="Streamlit App with Background Image", layout="wide")

# HTML and CSS to set a background image
background_image = """
<style>
.stApp {
    background-image: url("https://i.postimg.cc/DfxYKD4M/99264900.webp");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(background_image, unsafe_allow_html=True)

# Example content to see the effect
st.title("Welcome to My Streamlit App")
st.write("This is an example of how to add a background image using HTML and CSS.")


# Create a sidebar for navigation
page = st.sidebar.selectbox("Choose a page", ["Predict", "Explore"])

# Show the selected page
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()



      