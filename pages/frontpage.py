import streamlit as st

# Page Configuration
st.set_page_config(page_title="Startup Success Predictor", layout="wide")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Benchmarks", "Predictor", "Visualizations", "About"])

# Home Page
if page == "Home":
    st.title("Welcome to the Startup Success Predictor")
    st.write("""
    This app helps startups and investors benchmark their performance and predict the likelihood of success based on industry data.
    Navigate through the sections to explore various features.
    """)
