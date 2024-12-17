import streamlit as st
import pandas as pd
import os

# Path to the data folder
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "../data/raw")

# Streamlit sidebar to select a file
st.sidebar.header("Select a Dataset")
files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(('.csv', '.json', '.xlsx'))]
selected_file = st.sidebar.selectbox("Available Files", files)

# Load the selected file
if selected_file:
    file_path = os.path.join(DATA_FOLDER, selected_file)

    st.title("Data Viewer")
    st.subheader(f"Displaying: {selected_file}")

    # Handle CSV, JSON, and Excel formats
    if selected_file.endswith(".csv"):
        data = pd.read_csv(file_path)
        data = data.sample(n=1000) 
        st.dataframe(data)
    elif selected_file.endswith(".json"):
        data = pd.read_json(file_path)
        st.dataframe(data)
    elif selected_file.endswith(".xlsx"):
        data = pd.read_excel(file_path)
        st.dataframe(data)
    else:
        st.error("Unsupported file format.")


