# titanic_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache  # Cache the data to speed up loading
def load_data():
    data = sns.load_dataset('titanic')  # Load the Titanic dataset from seaborn
    return data

data = load_data()

def main():
    st.title("Titanic Dataset Dashboard")
    st.write("Explore the Titanic dataset and its visualizations.")

    # Show the data
    if st.checkbox("Show raw data"):
        st.write(data)

    # Visualization 1: Passenger Class Distribution
    st.subheader("Passenger Class Distribution")
    class_counts = data['pclass'].value_counts()
    st.bar_chart(class_counts)

    # Visualization 2: Survival Rate by Gender
    st.subheader("Survival Rate by Gender")
    survival_rate = data.groupby('sex')['survived'].mean()
    st.bar_chart(survival_rate)

    # Visualization 3: Age Distribution
    st.subheader("Age Distribution")
    plt.figure(figsize=(10, 5))
    sns.histplot(data['age'].dropna(), bins=30, kde=True)
    st.pyplot(plt)

if __name__ == "__main__":
    main()
