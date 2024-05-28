import streamlit as st
import requests
import datetime

st.markdown('''
Please complete the form to see the startup success prediction.
''')

with st.form("User input form", clear_on_submit=True, border=True):
    founded_date = st.date_input('The company founded year',
                                    datetime.date(2019, 7, 6))

    location = st.selectbox("Select location", ['Baden-Wurttemberg',
                            'Bayern',
                            'Berlin',
                            'Brandenburg',
                            'Bremen',
                            'Hamburg',
                            'Hessen',
                            'Mecklenburg-Vorpommern',
                            'Niedersachsen',
                            'Nordrhein-Westfalen',
                            'Rheinland-Pfalz',
                            'Saarland',
                            'Sachsen',
                            'Sachsen-Anhalt',
                            'Schleswig-Holstein',
                            'Thuringen'])
    company_size = st.radio('Select company size',
                            ('10001+', '1001-5000',
                                '101-250', '11-50',
                                '251-500', '5001-10000',
                            '501-1000', '51-100'))
    industry = st.selectbox('Select industry', ['Sustainability',
                            'Navigation and Mapping',
                            'Advertising',
                            'Community and Lifestyle',
                            'Payments',
                            'Professional Services',
                            'Other',
                            'Consumer Electronics',
                            'Clothing and Apparel',
                            'Agriculture and Farming',
                            'Hardware',
                            'Software',
                            'Consumer Goods',
                            'Gaming',
                            'Content and Publishing',
                            'Internet Services',
                            'Events',
                            'Messaging and Telecommunications',
                            'Financial Services',
                            'Biotechnology',
                            'Sports',
                            'Data and Analytics',
                            'Manufacturing',
                            'Travel and Tourism',
                            'Real Estate',
                            'Transportation',
                            'Natural Resources',
                            'Artificial Intelligence (AI)',
                            'Energy',
                            'Education',
                            'Blockchain and Cryptocurrency',
                            'Sales and Marketing',
                            'Food and Beverage',
                            'Mobile',
                            'Privacy and Security',
                            'Apps',
                            'Information Technology',
                            'Design',
                            'Administrative Services',
                            'Media and Entertainment',
                            'Health Care',
                            'Government and Military',
                            'Commerce and Shopping',
                            'Science and Engineering',
                            'Lending and Investments',
                            'Video',
                            'Platforms',
                            'Music and Audio',
                            'Social Impact'])

    total_funding = st.number_input('Total Funding Amount (in USD)', min_value=0)

    st.markdown('''
                Please indicate the channels of social activity.
                ''')
    social_activity_wb = st.checkbox('Website')
    social_activity_ph = st.checkbox('Phone Number')
    social_activity_em = st.checkbox('Contact Email')
    social_activity_ln = st.checkbox('LinkedIn')
    social_activity_tw = st.checkbox('Twitter')
    social_activity_fb = st.checkbox('Facebook')

    st.form_submit_button(label="Submit")



params = {
    "founded_date": founded_date,
    "location": location,
    "company_size": company_size,
    "industry": industry,
    "total_funding": total_funding,
    "social_activity": [social_activity_wb,
                        social_activity_ph,
                        social_activity_em,
                        social_activity_ln,
                        social_activity_tw,
                        social_activity_fb]
}


st.write(params)
