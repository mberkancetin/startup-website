import streamlit as st
import pandas as pd
import plotly.express as px

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Exit Strategies 🚀")

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
        'Industry': ['Tech', 'Health', 'Finance', 'Education'],
        'Average Exit Time (Years)': [5, 7, 6, 8],
        'Success Rate (%)': [60, 70, 65, 55],
        'Recommended Strategy': ['IPO', 'Acquisition', 'Merger', 'Acquisition']
    }
    benchmark_df = pd.DataFrame(benchmark_data)

    # Eingabewerte als DataFrame
    input_data = {
        'Industry': [industry],
        'Average Exit Time (Years)': [company_age],  # Beispiel: Company Age als Proxy für Exit Time
        'Success Rate (%)': [funding_amount / 10000],  # Beispiel: Funding Amount als Proxy für Success Rate
        'Recommended Strategy': ['IPO']  # Beispiel: Feste Strategie
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with the industry benchmark")

    # Bar Chart für den Vergleich der Average Exit Time
    fig1 = px.bar(benchmark_df, x='Industry', y='Average Exit Time (Years)', title='Average Exit Time by Industry')
    fig1.add_scatter(x=input_df['Industry'], y=input_df['Average Exit Time (Years)'], mode='markers+text', text=input_df['Average Exit Time (Years)'], textposition='top center', name='Input Data')
    st.plotly_chart(fig1, use_container_width=True)

    # Bar Chart für den Vergleich der Success Rate
    fig2 = px.bar(benchmark_df, x='Industry', y='Success Rate (%)', title='Success Rate by Industry')
    fig2.add_scatter(x=input_df['Industry'], y=input_df['Success Rate (%)'], mode='markers+text', text=input_df['Success Rate (%)'], textposition='top center', name='Input Data')
    st.plotly_chart(fig2, use_container_width=True)

    # Tabelle für die empfohlene Exit-Strategie
    st.write("Tailored Recommendation for an Exit Strategy")
    st.write(input_df[['Industry', 'Recommended Strategy']])

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
