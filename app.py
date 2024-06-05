import streamlit as st
import requests
import datetime
import pandas as pd

#st.logo("images/startorb.jpg")

# with open("/root/code/mberkancetin/startup-website/style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('''
            ## StartOrb: Unlocking Tomorrow's Success Today
            Harness the Power of Data to Illuminate Your Startup Journey
''')

# “Predicting Success with StartOrb”

st.image('images/orb.gif')

# col1, col2 = st.columns(2)
col1, col2, col3 = st.columns(3)

with col2:
    if st.button("Success Prediction"):
        st.switch_page("pages/predictor.py")
        st.switch_page("pages/Success Predictor.py")
