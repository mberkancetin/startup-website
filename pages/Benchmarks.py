import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Industry Benchmarks 🏭")


# Beispiel für Benchmarking-Diagramme
st.write("Diagrams here")


#Check if entry values are existent in session state
if 'company_age' in st.session_state and 'funding_stage' in st.session_state and 'industry' in st.session_state and 'funding_amount' in st.session_state and 'number_of_articles' in st.session_state:
    company_age = st.session_state.company_age
    company_region = st.session_state.company_region
    last_funding = st.session_state.last_funding
    founded_date = st.session_state.founded_date
    funding_stage = st.session_state.funding_stage
    industry = st.session_state.industry
    funding_amount = st.session_state.funding_amount
    number_of_articles = st.session_state.number_of_articles


    # Example data
    benchmark_data = {
        'Company Age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Funding Amount': [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000],
        'Last Funding': [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
        'Number of Articles': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    }
    benchmark_df = pd.DataFrame(benchmark_data)


    # Input data as df
    input_data = {
        'Metric': ['Company Age', 'Funding Amount', 'Last Funding', 'Number of Articles'],
        'Value': [company_age, funding_amount, last_funding, number_of_articles]
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with the industry benchmark")

    #Bar chart
    fig = px.bar(benchmark_df, x=benchmark_df.index, y=['Company Age', 'Funding Amount', 'Last Funding', 'Number of Articles'],
                 title='Benchmark Data', labels={'value': 'Value', 'index': 'Benchmark Index'})
    fig.add_scatter(x=input_df['Metric'], y=input_df['Value'], mode='markers+text', text=input_df['Value'], textposition='top center', name='Input Data')
    st.plotly_chart(fig, use_container_width=True)

    # Line Chart
    fig2 = px.line(benchmark_df, x=benchmark_df.index, y=['Company Age', 'Funding Amount', 'Last Funding', 'Number of Articles'],
                   title='Benchmark Data Over Time', labels={'value': 'Value', 'index': 'Benchmark Index'})
    fig2.add_scatter(x=input_df['Metric'], y=input_df['Value'], mode='markers+text', text=input_df['Value'], textposition='top center', name='Input Data')
    st.plotly_chart(fig2, use_container_width=True)


#Save variables in session state
    st.session_state.company_age = company_age
    st.session_state.company_region = company_region
    st.session_state.founded_date = founded_date
    st.session_state.funding_stage = funding_stage
    st.session_state.last_funding = last_funding
    st.session_state.industry = industry
    st.session_state.funding_amount = funding_amount
    st.session_state.number_of_articles = number_of_articles
else:
    st.warning("Please enter the required information on the input")


################################## BUZZ ########################################



# Set the style
plt.style.use('fivethirtyeight')

# Convert 'articles' column to numeric, forcing errors to NaN, then drop NaNs and 0 values
df_final['articles'] = pd.to_numeric(df_final['articles'], errors='coerce')
df_articles_filtered = df_final.dropna(subset=['articles'])
df_articles_filtered = df_articles_filtered[df_articles_filtered['articles'] > 0]

# Specify the funding round to analyze
funding_round = 'Series B'

# Filter the dataframe for the specified funding round
df_round_filtered = df_articles_filtered[df_articles_filtered['last_funding_type'] == funding_round]

# Calculate statistics for the funding round
mean_articles = df_round_filtered['articles'].mean()
std_articles = df_round_filtered['articles'].std()
stats = {
    'Min': df_round_filtered['articles'].min(),
    '25th percentile': df_round_filtered['articles'].quantile(0.25),
    'Median': df_round_filtered['articles'].median(),
    '75th percentile': df_round_filtered['articles'].quantile(0.75),
    '1 SD Above Mean': mean_articles + 1 * std_articles,
    '2 SD Above Mean': mean_articles + 2 * std_articles
}

# Define a hypothetical company
hypothetical_company_articles = 30

# Combine stats and hypothetical company
all_values = list(stats.values()) + [hypothetical_company_articles]
all_labels = list(stats.keys()) + ['Your Company']
sorted_indices = np.argsort(all_values)

sorted_values = np.array(all_values)[sorted_indices]
sorted_labels = np.array(all_labels)[sorted_indices]

# Create the lollipop chart
plt.figure(figsize=(12, 6))

# Plot the lollipop chart
for i, value in enumerate(sorted_values):
    color = 'red' if sorted_labels[i] == 'Your Company' else 'blue'
    plt.hlines(y=sorted_labels[i], xmin=0, xmax=value, color=color, alpha=0.7)
    plt.plot(value, sorted_labels[i], 'o', color=color)

# Set the labels and title
plt.xlabel('Number of Articles')
plt.title('Buzz Surrounding Companies in Series B')

st.pyplot(plt)

############################## Mean Growth Ratio by Industry Group and Funding Stage############


# Set the style
plt.style.use('fivethirtyeight')

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
ax = sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', cbar_kws={'label': 'Mean Growth Ratio'}, linewidths=.5)

# Add a marker for "Your Company"
your_company_industry = 'Health and Biotechnology'
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


####################### Mean total funding by industry group and funding strage ###########################

# Set the style
plt.style.use('fivethirtyeight')

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
heatmap_data = melted_df.pivot('industry_groups', 'Funding Stage', 'Mean Total Funding')
ax = sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='YlGnBu', cbar_kws={'label': 'Mean Total Funding (USD)'}, linewidths=.5)

# Add a marker for "Your Company"
your_company_industry = 'Health and Biotechnology'
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

# Save the figure
#plt.savefig('/Users/andreas/Desktop/03 - Le Wagon/Data ViZ/mean_total_funding_heat_map_with_your_company.png', dpi=300, bbox_inches='tight')

# Show the figure
st.pyplot(plt)

#################################### Estimated Company Valuation for Companies NEEDS TO BE UPDATED - STILL FOR REVENUE #################


# Set the style
plt.style.use('fivethirtyeight')

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

# Save the figure
#plt.savefig('/Users/andreas/Desktop/03 - Le Wagon/Data ViZ/angular_gauge_chart.png', dpi=300, bbox_inches='tight')

# Show the figure
plt.show()


#Background Picture for more swag

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
