import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Exit Strategies 🚀")

# Sample benchmark data
benchmark_data = {
    'Industry': ['Tech', 'Healthcare', 'Finance', 'Retail', 'Energy and Natural Resources'],
    'Average Exit Time (Years)': [8, 10, 7, 12, 10],
    'Success Rate (%)': [60, 30, 25, 40, 75]
}
benchmark_df = pd.DataFrame(benchmark_data)

# Check if entry values are existent in session state
if 'founded_date' in st.session_state and 'next_stage_funding' in st.session_state and 'industry' in st.session_state:
    location = st.session_state.location
    location_city = st.session_state.location_city
    company_size = st.session_state.company_size
    no_founders = st.session_state.no_founders
    funding_status = st.session_state.funding_status
    revenue_range = st.session_state.revenue_range
    founded_date = st.session_state.founded_date
    next_stage_funding = st.session_state.next_stage_funding
    has_debt_financing = st.session_state.has_debt_financing
    has_grant = st.session_state.has_grant
    industry = st.session_state.industry

    # Eingabewerte als DataFrame
    input_data = {
        'Industry': [industry],
        'Average Exit Time (Years)': [(datetime.date.today() - founded_date).days / 365],  # Beispiel: Berechnung der Firmenalter in Jahren
        'Success Rate (%)': [60],  # Beispiel: Next Stage Funding als Proxy für Success Rate
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
