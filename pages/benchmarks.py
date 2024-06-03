import streamlit as st

st.title("Benchmarks")

funding_amount = st.number_input("Funding Amount", min_value=0)
investment_stage = st.selectbox("Investment Stage", ["Pre-Seed", "Seed", "Series A", "Series B", "Series C"])
industry = st.selectbox("Industry", ["Tech", "Health", "Finance", "Education", "Other"])
company_age = st.number_input("Company Age", min_value=0)
number_of_articles = st.number_input("Number of Articles", min_value=0)

# Beispiel für Benchmarking-Diagramme
st.write("Benchmarking-Diagramme werden hier angezeigt.")
