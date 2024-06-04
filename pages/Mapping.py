import streamlit as st
import pandas as pd

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Map 🗺️")

# Check if entry values are existent in session state
if 'company_age' in st.session_state and 'funding_stage' in st.session_state and 'industry' in st.session_state and 'funding_amount' in st.session_state and 'number_of_articles' in st.session_state:
    company_age = st.session_state.company_age
    company_region = st.session_state.company_region
    last_funding = st.session_state.last_funding
    founded_date = st.session_state.founded_date
    funding_stage = st.session_state.funding_stage
    industry = st.session_state.industry
    funding_amount = st.session_state.funding_amount
    number_of_articles = st.session_state.number_of_articles

    # Beispielhafte Benchmark-Daten
    benchmark_data = {
        'lat': [37.7749, 40.7128, 34.0522, 51.5074, 48.8566],
        'lon': [-122.4194, -74.0060, -118.2437, -0.1278, 2.3522],
        'City': ['San Francisco', 'New York', 'Los Angeles', 'London', 'Paris'],
        'Investment Amount': [5000000, 7000000, 3000000, 4000000, 6000000]
    }
    benchmark_df = pd.DataFrame(benchmark_data)

    # Eingabewerte als DataFrame
    input_data = {
        'lat': [37.7749],  # Example latitude for the input data
        'lon': [-122.4194],  # Example longitude for the input data
        'City': ['San Francisco'],  # Example city for the input data
        'Investment Amount': [funding_amount]
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with the industry benchmark")

    # Karte mit den Standorten der Startups
    st.map(benchmark_df)

    # Analyse der geografischen Verteilung der Investitionen
    st.write("Geographical Distribution of Funding")
    st.write(benchmark_df)

    # Identifikation von aufstrebenden Startup-Hubs
    st.write("Rising Startup-Hubs")
    st.write(benchmark_df[benchmark_df['Investment Amount'] > 4000000])

    # Vergleich der Eingabewerte mit den Benchmark-Daten
    st.write("Comparison with Your Data")
    st.write(input_df)

    # Visualisierung der Eingabewerte auf der Karte
    st.map(input_df)

else:
    st.warning("Please enter the required information on the input page")

# Hintergrundbild einfügen
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 1)), url('https://pplx-res.cloudinary.com/image/upload/v1717425816/user_uploads/rsbszhwcj/orb.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

