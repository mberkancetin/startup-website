import streamlit as st


if st.button("Home"):
    st.switch_page("startup-success-interface/app.py")

st.write('This is page 2')
