import streamlit as st
import pandas as pd
import plotly.express as px

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Funding Trends 💰📈")

# Überprüfen, ob die Eingaben im Session State vorhanden sind
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
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Funding Amount': [1000000, 1500000, 2000000, 2500000, 3000000],
        'Industry': ['Tech', 'Health', 'Finance', 'Education', 'Tech'],
        'Region': ['North America', 'Europe', 'Asia', 'North America', 'Europe'],
        'Investment Stage': ['Seed', 'Series A', 'Series B', 'Series C', 'Seed']
    }
    benchmark_df = pd.DataFrame(benchmark_data)

    # Eingabewerte als DataFrame
    input_data = {
        'Year': [founded_date.year],
        'Funding Amount': [funding_amount],
        'Industry': [industry],
        'Region': [company_region],
        'Investment Stage': [funding_stage]
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with the industry benchmark")

    # Zeitliche Entwicklung der Finanzierungsrunden
    fig1 = px.line(benchmark_df, x='Year', y='Funding Amount', title='Funding Amount Over Years')
    fig1.add_scatter(x=input_df['Year'], y=input_df['Funding Amount'], mode='markers+text', text=input_df['Funding Amount'], textposition='top center', name='Input Data')
    st.plotly_chart(fig1, use_container_width=True)

    # Vergleich der Finanzierungsbeträge nach Branchen und Regionen
    fig2 = px.bar(benchmark_df, x='Industry', y='Funding Amount', color='Region', title='Funding Amount by Industry and Region')
    fig2.add_scatter(x=input_df['Industry'], y=input_df['Funding Amount'], mode='markers+text', text=input_df['Funding Amount'], textposition='top center', name='Input Data')
    st.plotly_chart(fig2, use_container_width=True)

    # Analyse der häufigsten Investitionsphasen
    fig3 = px.histogram(benchmark_df, x='Investment Stage', title='Investment Stages Distribution')
    fig3.add_scatter(x=input_df['Investment Stage'], y=[1], mode='markers+text', text=input_df['Investment Stage'], textposition='top center', name='Input Data')
    st.plotly_chart(fig3, use_container_width=True)

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
