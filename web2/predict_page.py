import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords

# Load the necessary files
with open(r'C:\Users\mohameds\OneDrive\Documents\GitHub\MAIN_CV_PROJECTS\web2\random_forest_rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open(r'C:\Users\mohameds\OneDrive\Documents\GitHub\MAIN_CV_PROJECTS\web2\tfidf_rf.pkl', 'rb') as vectorizer_file:
    tfidf = pickle.load(vectorizer_file)

# Ensure stopwords are downloaded
nltk.download('stopwords')

# Function to preprocess and vectorize the input text
def preprocess_and_vectorize(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return tfidf.transform([text])

def show_predict_page():
    st.title("YouTube Spam Detection")

    input_comment = st.text_area("Enter a YouTube comment:")

    if st.button("Predict"):
        if input_comment:
            vectorized_comment = preprocess_and_vectorize(input_comment)
            prediction = model.predict(vectorized_comment)
            prediction_proba = model.predict_proba(vectorized_comment)

            st.write("Prediction: ", "Spam" if prediction[0] == 1 else "Not Spam")
            st.write("Probability: ", prediction_proba[0])
        else:
            st.warning("Please enter a comment.")
