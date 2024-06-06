import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.style.use('dark_background')

# Daten laden
df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Industry Benchmarks 🏭")

# Beispiel für Benchmarking-Diagramme
st.write("Diagrams here")

if 'revenue_range' in st.session_state and 'industry' in st.session_state and 'total_funding' in st.session_state and 'company_size' in st.session_state:
    location = st.session_state.location
    location_city = st.session_state.location_city
    company_size = st.session_state.company_size
    no_founders = st.session_state.no_founders
    funding_status = st.session_state.funding_status
    revenue_range = st.session_state.revenue_range
    founded_date = st.session_state.founded_date
    next_stage_funding = st.session_state.next_stage_funding
    has_debt_financing = st.session_state.has_debt_financing
    has_grant = st.session_state.has_grant
    industry = st.session_state.industry

    input_data = {
        'Metric': ['Revenue Range', 'Industry', 'Total Funding', 'Company Size'],
        'Value': [revenue_range, industry, total_funding, company_size]
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with the industry benchmark")

    # Bar Chart
    fig = px.bar(df_final, x=df_final.index, y=['revenue_range', 'industry', 'total_funding_usd', 'no_employees'],
                 title='Benchmark Data', labels={'value': 'Value', 'index': 'Benchmark Index'})
    fig.add_scatter(x=input_df['Metric'], y=input_df['Value'], mode='markers+text', text=input_df['Value'], textposition='top center', name='Input Data')
    st.plotly_chart(fig, use_container_width=True)

    # Line Chart
    fig2 = px.line(df_final, x=df_final.index, y=['revenue_range', 'industry', 'total_funding_usd', 'no_employees'],
                   title='Benchmark Data Over Time', labels={'value': 'Value', 'index': 'Benchmark Index'})
    fig2.add_scatter(x=input_df['Metric'], y=input_df['Value'], mode='markers+text', text=input_df['Value'], textposition='top center', name='Input Data')
    st.plotly_chart(fig2, use_container_width=True)

    # Save variables in session state
    location = st.session_state.location
    location_city = st.session_state.location_city
    company_size = st.session_state.company_size
    no_founders = st.session_state.no_founders
    funding_status = st.session_state.funding_status
    revenue_range = st.session_state.revenue_range
    founded_date = st.session_state.founded_date
    total_funding = st.session_state.total_funding
    has_debt_financing = st.session_state.has_debt_financing
    has_grant = st.session_state.has_grant
    industry = st.session_state.industry
else:
    st.warning("Please enter the required information on the input page")

############################## Mean Growth Ratio by Industry Group and Funding Stage############

# List of funding ratio columns in chronological order
funding_ratios = ['seed_to_pre_ratio', 'a_to_seed_ratio', 'b_to_a_ratio', 'c_to_b_ratio', 'd_to_c_ratio', 'e_to_d_ratio']

# Calculate mean growth ratio for each industry group at each funding stage
mean_growth_ratios = df_final.groupby('industry_groups')[funding_ratios].mean().reset_index()

# Melt the DataFrame to make it suitable for a heat map
melted_df = mean_growth_ratios.melt(id_vars='industry_groups', var_name='Funding Stage', value_name='Mean Growth Ratio')

# Ensure the funding stages are in chronological order
melted_df['Funding Stage'] = pd.Categorical(melted_df['Funding Stage'], categories=funding_ratios, ordered=True)

# Create the heat map
plt.figure(figsize=(12, 8))
heatmap_data = melted_df.pivot(index='industry_groups', columns='Funding Stage', values='Mean Growth Ratio')
ax = sns.heatmap(heatmap_data, annot=True, cmap='viridis', cbar_kws={'label': 'Mean Growth Ratio'}, linewidths=.5)

# Add a marker for "Your Company"
your_company_industry = 'Energy and Natural Resources'
your_company_stage = 'b_to_a_ratio'
plt.scatter(funding_ratios.index(your_company_stage) + 0.5,
            heatmap_data.index.get_loc(your_company_industry) + 0.2,
            color='red', s=100, zorder=5)
plt.text(funding_ratios.index(your_company_stage) + 0.55,
         heatmap_data.index.get_loc(your_company_industry),
         ' Your Company', color='red', fontsize=14, rotation=15, ha='left', va='center')

# Labels and title
plt.xlabel('Funding Stage')
plt.ylabel('Industry Groups')
plt.title('Mean Growth Ratio by Industry Group and Funding Stage')

# Adjust x-axis labels for better readability
plt.xticks(rotation=45)

# Show the figure in Streamlit
st.pyplot(plt)

####################### Mean total funding by industry group and funding stage ###########################

# List of funding ratio columns in chronological order
funding_stages = ['preseed_fund', 'seed_fund', 'series_a_fund', 'series_b_fund', 'series_c_fund', 'series_d_fund', 'series_e_fund']

# Calculate mean total funding for each industry group at each funding stage
mean_funding = df_final.groupby('industry_groups')[funding_stages].mean().reset_index()

# Melt the DataFrame to make it suitable for a heat map
melted_df = mean_funding.melt(id_vars='industry_groups', var_name='Funding Stage', value_name='Mean Total Funding')

# Ensure the funding stages are in chronological order
melted_df['Funding Stage'] = pd.Categorical(melted_df['Funding Stage'], categories=funding_stages, ordered=True)

# Create the heat map
plt.figure(figsize=(12, 8))
heatmap_data = melted_df.pivot(index='industry_groups', columns='Funding Stage', values='Mean Total Funding')
ax = sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='viridis', cbar_kws={'label': 'Mean Total Funding (USD)'}, linewidths=.5)

# Add a marker for "Your Company"
your_company_industry = 'Healthcare and Biotechnology'
your_company_stage = 'series_b_fund'
plt.scatter(funding_stages.index(your_company_stage) + 0.5,
            heatmap_data.index.get_loc(your_company_industry) + 0.2,
            color='red', s=100, zorder=5)
plt.text(funding_stages.index(your_company_stage) + 0.55,
         heatmap_data.index.get_loc(your_company_industry),
         ' Your Company', color='red', fontsize=14, rotation=15, ha='left', va='center')

# Labels and title
plt.xlabel('Funding Stage')
plt.ylabel('Industry Groups')
plt.title('Mean Total Funding by Industry Group and Funding Stage')

# Adjust x-axis labels for better readability
plt.xticks(rotation=45)

# Show the figure in Streamlit
st.pyplot(plt)

#################################### Estimated Company Valuation for Companies NEEDS TO BE UPDATED - STILL FOR REVENUE #################

# Define the revenue ranges in ascending order
revenue_ranges = ['$1M to $10M', 'Less than $1M', '$10M to $50M', '$50M to $100M', '$100M to $500M', '$500M to $1B', '$1B to $10B', '$10B+']

# Sort the revenue ranges and remove NaN values
df_final = df_final.dropna(subset=['Estimated Revenue Range'])
df_final = df_final[df_final['Estimated Revenue Range'].isin(revenue_ranges)]

# Hypothetical "Your Company" details
your_company_revenue = '$50M to $100M'  # Example value

# Calculate the position of "Your Company" in the revenue ranges
your_company_index = revenue_ranges.index(your_company_revenue)

# Create the gauge chart
fig, ax = plt.subplots(figsize=(10, 5), subplot_kw={'projection': 'polar'})
theta = np.linspace(0, np.pi, len(revenue_ranges) + 1)

# Create the bars for the gauge
bars = ax.bar(theta[:-1], np.ones(len(revenue_ranges)), width=np.diff(theta), align='edge', color=plt.cm.viridis(np.linspace(0, 1, len(revenue_ranges))), edgecolor='black')

# Set the labels for the revenue ranges
ax.set_xticks(theta[:-1] + np.diff(theta) / 2)
ax.set_xticklabels(revenue_ranges, fontsize=10)

# Hide the radial labels and the frame
ax.set_yticklabels([])
ax.spines['polar'].set_visible(False)

# Add a pointer for "Your Company"
ax.plot([theta[your_company_index] + np.diff(theta)[0] / 2, theta[your_company_index] + np.diff(theta)[0] / 2], [0, 1.2], color='red', linewidth=3)
ax.text(theta[your_company_index] + np.diff(theta)[0] / 2, 1.25, 'Your Company', color='red', fontsize=12, ha='center')

# Title and layout adjustments
plt.title('Estimated Revenue Range for Companies', fontsize=15)
plt.tight_layout()

# Show the figure
st.pyplot(plt)

# Background Picture for more swag
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 1)), url('https://pplx-res.cloudinary.com/image/upload/v1717425816/user_uploads/rsbszhwcj/orb.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
