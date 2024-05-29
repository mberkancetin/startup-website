import streamlit as st
import requests

st.logo("images/startorb.jpg")

st.markdown('''
            ## StartOrb: Unlocking Tomorrow's Success Today
            Harness the Power of Data to Illuminate Your Startup Journey
''')

# “Predicting Success with StartOrb”

st.image('images/orb.gif')

col1, col2 = st.columns(2)

with col1:
    if st.button("Success Prediction"):
        st.switch_page("pages/predictor.py")

with col2:
    if st.button("Ecosystem Benchmarks"):
        st.switch_page("pages/benchmarks.py")
