import streamlit as st
import pandas as pd
import numpy as np


if st.button("Home"):
    st.switch_page("app.py")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Company Size", "Raised Funds", "Funding Rounds"])
chart_data['Location'] = np.random.choice(['East','West','North', 'South'], 20)

st.scatter_chart(
    chart_data,
    x='Company Size',
    y='Raised Funds',
    color='Location',
    size='Funding Rounds',
)



chart_data = pd.DataFrame(np.random.randn(20, 8), columns=['10001+', '1001-5000',
                                '101-250', '11-50',
                                '251-500', '5001-10000',
                            '501-1000', '51-100'])

st.area_chart(chart_data)
