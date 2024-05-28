import streamlit as st

col1, col2 = st.columns(2)

with col2:
    if st.button("Home"):
        st.switch_page("../app.py")

st.write('This is page 2')
