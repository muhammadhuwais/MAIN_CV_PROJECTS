import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:/Users/mohameds/OneDrive/Documents/GitHub/MAIN_CV_PROJECTS/web2/archive (8)/Youtube-Spam-Dataset.csv'
df = pd.read_csv(file_path)

def show_explore_page():
    st.title("Explore YouTube Spam Dataset")

    # Show the raw data
    if st.checkbox("Show Raw Data"):
        st.write(df)

    # Show basic statistics
    st.write("## Basic Statistics")
    st.write(df.describe())

    # Visualize the class distribution
    st.write("## Class Distribution")
    sns.countplot(x='CLASS', data=df)
    plt.title('Class Distribution')
    st.pyplot(plt.gcf())
    plt.clf()  # Clear the figure

    # Visualize the distribution of comment lengths
    df['comment_length'] = df['CONTENT'].apply(len)
    st.write("## Comment Length Distribution")
    sns.histplot(df['comment_length'], bins=50)
    plt.title('Comment Length Distribution')
    st.pyplot(plt.gcf())
    plt.clf()  # Clear the figure
