import streamlit as st

st.set_page_config(page_title="Startup Success Predictor", page_icon="🚀")

st.title("Willkommen zur Startup Success Predictor App")
st.write("""
Diese App hilft Startups und Investoren, den Erfolg von Startups zu bewerten und zu benchmarken.
Navigieren Sie durch die verschiedenen Seiten, um mehr zu erfahren.
""")

st.sidebar.title("Navigation")
st.sidebar.markdown("[Benchmarks](pages/benchmarks.py)")
st.sidebar.markdown("[Predictor](pages/predictor.py)")
st.sidebar.markdown("[Visualisierungen](pages/visualizations.py)")
st.sidebar.markdown("[Über uns](pages/about.py)")


