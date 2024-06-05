import streamlit as st
import requests
import datetime
import pandas as pd

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")


# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('''
            ## StartOrb: Unlocking Tomorrow's Success Today
            Harness the Power of Data to Illuminate Your Startup Journey
''')

st.image('images/orb.gif')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Success Prediction"):
        st.switch_page("pages/Success Predictor.py")

with col2:
    if st.button("Industry Benchmarks"):
        st.switch_page("pages/Benchmarks.py")

with col3:
    if st.button("Funding Trends"):
        st.switch_page("pages/Funding_Trends.py")

col4, col5 = st.columns(2)

with col4:
    if st.button("Map"):
        st.switch_page("pages/Mapping.py")

with col5:
    if st.button("Exit Strategies"):
        st.switch_page("pages/Exit Strategies.py")

st.title("Tell us more about your company")

# Initialize values in session state if no value is entered
if 'company_age' not in st.session_state:
    st.session_state.company_age = 0
if 'company_region' not in st.session_state:
    st.session_state.company_region = 'No Region'
if 'founded_date' not in st.session_state:
    st.session_state.founded_date = datetime.date(2019, 7, 6)
if 'founders' not in st.session_state:
    st.session_state.founders = 0
if 'funding_stage' not in st.session_state:
    st.session_state.funding_stage = 'No funding'
if 'last_funding' not in st.session_state:
    st.session_state.last_funding = 0
if 'industry' not in st.session_state:
    st.session_state.industry = 'No Industry'
if 'funding_amount' not in st.session_state:
    st.session_state.funding_amount = 0
if 'number_of_articles' not in st.session_state:
    st.session_state.number_of_articles = 0

# Define callback functions to update session state
def update_founded_date():
    st.session_state.founded_date = st.session_state.founded_date_input

def update_funding_amount():
    st.session_state.funding_amount = st.session_state.funding_amount_input

def update_last_funding():
    st.session_state.last_funding = st.session_state.last_funding_input

def update_funding_stage():
    st.session_state.funding_stage = st.session_state.funding_stage_input

def update_industry():
    st.session_state.industry = st.session_state.industry_input

def update_company_age():
    st.session_state.company_age = st.session_state.company_age_input

def update_company_region():
    st.session_state.company_region = st.session_state.company_region_input

def update_founders():
    st.session_state.founders = st.session_state.founders_input

def update_number_of_articles():
    st.session_state.number_of_articles = st.session_state.number_of_articles_input

# Enter values here
founded_date = st.date_input('The company founded year', value=st.session_state.founded_date, key="founded_date_input", on_change=update_founded_date)
funding_amount = st.number_input("Total Funding Amount", min_value=0, value=st.session_state.funding_amount, key="funding_amount_input", on_change=update_funding_amount)
last_funding = st.number_input("Last Funding Amount", min_value=0, value=st.session_state.last_funding, key="last_funding_input", on_change=update_last_funding)
investment_stage = st.selectbox("Investment Stage", [
    "Pre-Seed", "Seed", "Series A", "Series B", "Series C", "Private Equity", "Debt Financing",
    "Grants", "M&A", "IPO", 'No funding'
], index=["Pre-Seed", "Seed", "Series A", "Series B", "Series C", "Private Equity", "Debt Financing",
    "Grants", "M&A", "IPO", 'No funding'].index(st.session_state.funding_stage), key="funding_stage_input", on_change=update_funding_stage)
industry = st.selectbox("Industry", [
    "Technology and Software", "Retail and E-Commerce", "Business Services", "Finance and Payments",
    "Hardware and Electronics", "Healthcare and Biotechnology", "Energy and Natural Resources",
    "Consumer Products", "Manufacturing and Industry", "Telecommunications and Internet Services",
    "Community and Lifestyle", "Media and Entertainment", "Education and Training",
    "Transport and Logistics", "Government and Public Services", "Science and Engineering",
    "Travel and Tourism", "Other", "No Industry"
], index=["Technology and Software", "Retail and E-Commerce", "Business Services", "Finance and Payments",
    "Hardware and Electronics", "Healthcare and Biotechnology", "Energy and Natural Resources",
    "Consumer Products", "Manufacturing and Industry", "Telecommunications and Internet Services",
    "Community and Lifestyle", "Media and Entertainment", "Education and Training",
    "Transport and Logistics", "Government and Public Services", "Science and Engineering",
    "Travel and Tourism", "Other", "No Industry"].index(st.session_state.industry), key="industry_input", on_change=update_industry)
company_age = st.number_input("Company Age", min_value=0, value=st.session_state.company_age, key="company_age_input", on_change=update_company_age)
company_region = st.selectbox("Location", [
    'Baden-Wurttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen',
    'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz',
    'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thuringen', 'No Region'
], index=['Baden-Wurttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen',
    'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz',
    'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thuringen', 'No Region'].index(st.session_state.company_region), key="company_region_input", on_change=update_company_region)
founders = st.number_input("Founding Team Size", min_value=0, value=st.session_state.founders, key="founders_input", on_change=update_founders)
number_of_articles = st.number_input("Number of Articles", min_value=0, value=st.session_state.number_of_articles, key="number_of_articles_input", on_change=update_number_of_articles)

# Check if all fields are filled
if all([
    st.session_state.company_age,
    st.session_state.company_region,
    st.session_state.founded_date,
    st.session_state.founders,
    st.session_state.funding_stage,
    st.session_state.last_funding,
    st.session_state.industry,
    st.session_state.funding_amount,
    st.session_state.number_of_articles
]):
    st.success("Saved! The orb is happy to predict your success")
else:
    st.warning("Please enter a value for every row")
