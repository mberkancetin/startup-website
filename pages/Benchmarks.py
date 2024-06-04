import streamlit as st
import pandas as pd
import plotly.express as px

with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Industry Benchmarks 🏭")


# Beispiel für Benchmarking-Diagramme
st.write("Diagrams here")


#Check if entry values are existent in session state
if 'company_age' in st.session_state and 'funding_stage' in st.session_state and 'industry' in st.session_state and 'funding_amount' in st.session_state and 'number_of_articles' in st.session_state:
    company_age = st.session_state.company_age
    company_region = st.session_state.company_region
    last_funding = st.session_state.last_funding
    founded_date = st.session_state.founded_date
    funding_stage = st.session_state.funding_stage
    industry = st.session_state.industry
    funding_amount = st.session_state.funding_amount
    number_of_articles = st.session_state.number_of_articles


    # Example data
    benchmark_data = {
        'Company Age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Funding Amount': [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000],
        'Last Funding': [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
        'Number of Articles': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    }
    benchmark_df = pd.DataFrame(benchmark_data)


    # Input data as df
    input_data = {
        'Metric': ['Company Age', 'Funding Amount', 'Last Funding', 'Number of Articles'],
        'Value': [company_age, funding_amount, last_funding, number_of_articles]
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with the industry benchmark")

    #Bar chart
    fig = px.bar(benchmark_df, x=benchmark_df.index, y=['Company Age', 'Funding Amount', 'Last Funding', 'Number of Articles'],
                 title='Benchmark Data', labels={'value': 'Value', 'index': 'Benchmark Index'})
    fig.add_scatter(x=input_df['Metric'], y=input_df['Value'], mode='markers+text', text=input_df['Value'], textposition='top center', name='Input Data')
    st.plotly_chart(fig, use_container_width=True)

    # Line Chart
    fig2 = px.line(benchmark_df, x=benchmark_df.index, y=['Company Age', 'Funding Amount', 'Last Funding', 'Number of Articles'],
                   title='Benchmark Data Over Time', labels={'value': 'Value', 'index': 'Benchmark Index'})
    fig2.add_scatter(x=input_df['Metric'], y=input_df['Value'], mode='markers+text', text=input_df['Value'], textposition='top center', name='Input Data')
    st.plotly_chart(fig2, use_container_width=True)


#Save variables in session state
    st.session_state.company_age = company_age
    st.session_state.company_region = company_region
    st.session_state.founded_date = founded_date
    st.session_state.funding_stage = funding_stage
    st.session_state.last_funding = last_funding
    st.session_state.industry = industry
    st.session_state.funding_amount = funding_amount
    st.session_state.number_of_articles = number_of_articles
else:
    st.warning("Please enter the required information on the input")





#Background Picture for more swag

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
