import streamlit as st
import pandas as pd

def show_explore_page():
    st.title("Explore the Sonar Dataset")

    # Load the dataset (assuming it's stored locally)
    df = pd.read_csv(r"C:\Users\mohameds\OneDrive\Documents\GitHub\MAIN_CV_PROJECTS\web_\sonar.csv")  # Replace with your actual dataset path
    
    st.write("### Dataset Preview")
    st.dataframe(df.head())
    
    st.write("### Basic Statistics")
    st.write(df.describe())
    
    st.write("### Class Distribution")
    st.bar_chart(df.iloc[:, -1].value_counts())  # Assuming the last column is the target
    
    # Add more EDA visualizations as needed
