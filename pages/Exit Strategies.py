import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

df_final = pd.read_csv("raw_data/X_y_data3.csv")

# Einbinden des benutzerdefinierten CSS
with open("style.css") as f: # Benedikt's tmp comment: /code/mberkancetin/startup-website/
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Exit Strategies 🚀")

# Sample benchmark data
benchmark_data = {
    'Industry': ['Tech', 'Healthcare', 'Finance', 'Retail', 'Energy & Natural<br>Resources'],
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
    # success_prediction = st.session_state.success_prediction

    # Eingabewerte als DataFrame
    input_data = {
        'Industry': ['Energy & Natural<br>Resources'], #BEN COMMENT: this is hardcorded. Before, the word industry w/o quotation marks was within in the brackets
        'Average Exit Time (Years)': [4.9], #BEN COMMENTED FOLLOWING:[round((datetime.date.today() - founded_date).days / 365, ndigits=1)],
        'Success Rate (%)': [60],  # Beispiel: Next Stage Funding als Proxy für Success Rate
        'Recommended Strategy': ['Initial Public Offering']  # Beispiel: Feste Strategie
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with industry benchmarks")

    # Bar Chart für den Vergleich der Average Exit Time
    fig1 = px.bar(benchmark_df, x='Industry', y='Average Exit Time (Years)', title='Average Exit Time by Industry')
    fig1.add_scatter(
        x=input_df['Industry'],
        y=input_df['Average Exit Time (Years)'],
        mode='markers+text',
        text="Your company:<br>4.9 years old",#BEN COMMENTED THE FOLLOWING: input_df['Average Exit Time (Years)'],
        textposition='top center',
        #name='Your company',
        marker=dict(color='red'),
        textfont=dict(color='white'),
        showlegend=False
    )

    #BENEDIKT: ADDING HORIZONTAL AND VERTICAL LINES FIG 1 START
    x_point = 'Energy & Natural<br>Resources'
    y_point = 4.9
    # Add vertical dashed line
    fig1.add_shape(
        type='line',
        x0=x_point,
        y0=0,
        x1=x_point,
        y1=y_point,
        line=dict(
            color='red',
            width=2,
            dash='dash'
        )
    )
    # Add horizontal dashed line
    fig1.add_shape(
        type='line',
        x0=-0.4,
        y0=y_point,
        x1=x_point,
        y1=y_point,
        line=dict(
            color='red',
            width=2,
            dash='dash'
        )
    )
    fig1.update_xaxes(type='category')
    #BENEDIKT: ADDING HORIZONTAL AND VERTICAL LINES FIG 1 STOP
    st.plotly_chart(fig1, use_container_width=True)

    # Bar Chart für den Vergleich der Success Rate
    fig2 = px.bar(benchmark_df, x='Industry', y='Success Rate (%)', title='Probability of successful Exit by Industry')
    fig2.add_scatter(
        x=input_df['Industry'],
        y=input_df['Success Rate (%)'],
        mode='markers+text',
        text="Your company:<br>60%",
        textposition='top center',
        name='Your company',
        marker=dict(color='red'),
        textfont=dict(color='white', size=12),
        showlegend=False
    )
    #BENEDIKT: ADDING HORIZONTAL AND VERTICAL LINES FIG 2 START
    x_point = 'Energy & Natural<br>Resources'
    y_point = 60
    # Add vertical dashed line
    fig2.add_shape(
        type='line',
        x0=x_point,
        y0=0,
        x1=x_point,
        y1=y_point,
        line=dict(
            color='red',
            width=2,
            dash='dash'
        )
    )
    # Add horizontal dashed line
    fig2.add_shape(
        type='line',
        x0=-0.4,
        y0=y_point,
        x1=x_point,
        y1=y_point,
        line=dict(
            color='red',
            width=2,
            dash='dash'
        )
    )
    fig2.update_xaxes(type='category')
    #BENEDIKT: ADDING HORIZONTAL AND VERTICAL LINES FIG 2 END
    st.plotly_chart(fig2, use_container_width=True)



    # Tabelle für die empfohlene Exit-Strategie
    st.subheader(" :rocket: Tailored recommendation for your exit strategy :rocket: ")
    tmp_df = input_df[['Industry', 'Recommended Strategy']]
    st.markdown(tmp_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

################BEN new approach to EXIT RECOMMENDATION START###################
    # st.subheader("Tailored Recommendation for your company's Exit Strategy")
    # st.markdown("Our reccommendation for a pre-seed company in the Energy & Natural Resources Industry: IPO")
################BEN new approach to EXIT RECOMMENDATION END###################


    # ########## new chart start Berkan
    # st.bar_chart(data= input_df,x='Industry', y='Success Rate (%)')
    # ########## new chart end Berkan

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
