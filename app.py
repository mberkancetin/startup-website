import streamlit as st
import requests

st.markdown('''
AI Powered Startup Success Prediction Tool.
''')

# StartOrb: Unlocking Tomorrow’s Success Today
# “Predicting Success with StartOrb”
# Subheadline: “Harness the Power of Data to Illuminate Your Startup Journey”
st.image('images/orb.gif', caption='Orb gif image')

col1, col2 = st.columns(2)

with col1:
    if st.button("Success Prediction"):
        st.switch_page("pages/predictor.py")

with col2:
    if st.button("Ecosystem Benchmarks"):
        st.switch_page("pages/benchmarks.py")
