import streamlit as st
import pandas as pd
import numpy as np

#st.logo("images/startorb.jpg")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write("# StartOrb")


st.image('images/saruman.gif', use_column_width=True)

st.write("")

st.markdown(
    f"""
    <div style="text-align: center; font-size: 36px;">
        May your ventures be as bright as the two trees of Valinor, and may success find you as surely as the ring found its way back to the fires of Mount Doom.

    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")


if st.button("Let's Predict Again"):
        st.switch_page("app.py")
