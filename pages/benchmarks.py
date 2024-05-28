import streamlit as st


if st.button("Home"):
    st.switch_page("app.py")

st.write('This is page 2')
