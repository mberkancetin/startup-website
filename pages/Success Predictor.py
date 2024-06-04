import streamlit as st
import requests
import datetime
import time
import random

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Center and enlarge the text
st.markdown(
    """
    <div style="text-align: center; font-size: 24px;">
        Are you ready to see your overall success prediction?
    </div>
    <br><br>
    <div style="text-align: center; font-size: 18px; margin-bottom: 30px;">
       The Orb will compare your company based on various parameters and give a score between 0 and 1, with 1 representing success
    </div>
    """,
    unsafe_allow_html=True
)

# Extract input data from session state
if 'company_age' in st.session_state and 'funding_stage' in st.session_state and 'industry' in st.session_state and 'funding_amount' in st.session_state and 'number_of_articles' in st.session_state:
    company_age = st.session_state.company_age
    company_region = st.session_state.company_region
    last_funding = st.session_state.last_funding
    founded_date = st.session_state.founded_date
    funding_stage = st.session_state.funding_stage
    industry = st.session_state.industry
    funding_amount = st.session_state.funding_amount
    number_of_articles = st.session_state.number_of_articles

    # Button for success prediction
    if st.button("Success Prediction"):
        # Clear the page
        st.empty()

        # Display the animation
        st.image('images/orb.gif', use_column_width=True)
        time.sleep(5)  # Wait for 5 seconds

        # Generate a random number between 0 and 1 for the success prediction
        success_prediction = round(random.uniform(0, 1), 2)

        # Display the success prediction
        st.markdown(
            f"""
            <div style="text-align: center; font-size: 24px;">
                Your Success Prediction Score: {success_prediction}
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.warning("Please enter the required information on the input page")


