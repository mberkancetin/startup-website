import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Funding Trends 💰📈")

# Überprüfen, ob die Eintragswerte im Session State vorhanden sind
if 'founded_date' in st.session_state and 'next_stage_funding' in st.session_state and 'industry' in st.session_state and 'location' in st.session_state and 'funding_status' in st.session_state:
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

    # Beispielhafte Benchmark-Daten
    benchmark_data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Funding Amount': [1000000, 1500000, 2000000, 2500000, 3000000],
        'Industry': ['Tech', 'Health', 'Finance', 'Education', 'Tech'],
        'Region': ['North America', 'Europe', 'Asia', 'North America', 'Europe'],
        'Investment Stage': ['Seed', 'Series A', 'Series B', 'Series C', 'Seed']
    }
    benchmark_df = pd.DataFrame(benchmark_data)

    # Eingabewerte als DataFrame
    input_data = {
        'Year': [founded_date.year],
        'Funding Amount': [next_stage_funding],
        'Industry': [industry],
        'Region': [location],
        'Investment Stage': [funding_status]
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with the industry benchmark")

    # Zeitliche Entwicklung der Finanzierungsrunden
    fig1 = px.line(benchmark_df, x='Year', y='Funding Amount', title='Funding Amount Over Years')
    fig1.add_scatter(x=input_df['Year'], y=input_df['Funding Amount'], mode='markers+text', text=input_df['Funding Amount'], textposition='top center', name='Input Data')
    st.plotly_chart(fig1, use_container_width=True)

    # Vergleich der Finanzierungsbeträge nach Branchen und Regionen
    fig2 = px.bar(benchmark_df, x='Industry', y='Funding Amount', color='Region', title='Funding Amount by Industry and Region')
    fig2.add_scatter(x=input_df['Industry'], y=input_df['Funding Amount'], mode='markers+text', text=input_df['Funding Amount'], textposition='top center', name='Input Data')
    st.plotly_chart(fig2, use_container_width=True)

    # Analyse der häufigsten Investitionsphasen
    fig3 = px.histogram(benchmark_df, x='Investment Stage', title='Investment Stages Distribution')
    fig3.add_scatter(x=input_df['Investment Stage'], y=[1], mode='markers+text', text=input_df['Investment Stage'], textposition='top center', name='Input Data')
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.warning("Please enter the required information on the input page")

#################### DISTRIBUTION OF MONTHS SINCE FOUNDED BY FUNDING TYPE  ############################

desired_funding_types = {
    'Pre-Seed': 'Pre-Seed',
    'Seed': 'Seed',
    'Series A': 'A',
    'Series B': 'B',
    'Series C': 'C',
    'Series D': 'D',
    'Series E': 'E',
    'Private Equity': 'Private Equity'
}

# Update the 'last_funding_type' column to combine all rounds after Series E into "Private Equity"
df_final['last_funding_type'] = df_final['last_funding_type'].replace(['Series F', 'Series G'], 'Private Equity')

# Filter out rows with invalid or missing values for 'months_since_founded'
df_final = df_final[np.isfinite(df_final['months_since_founded'])]

# Set plot style
plt.style.use('fivethirtyeight')

# Create combined KDE plot for all funding types
plt.figure(figsize=(14, 8))

# Iterate through each funding type and plot the KDE
for funding_type, short_label in desired_funding_types.items():
    subset = df_final[df_final['last_funding_type'] == funding_type]
    sns.kdeplot(subset['months_since_founded'], label=funding_type, shade=True)

    # Calculate and plot the median
    median = subset['months_since_founded'].median()
    plt.axvline(median, linestyle='--', color='gray', linewidth=1, label='_nolegend_')
    plt.text(median, plt.ylim()[1]*0.9, f'{short_label}: {median:.0f} months', rotation=90, verticalalignment='center')

plt.title('Distribution of Months Since Founded by Funding Type')
plt.xlabel('Months Since Founded')
plt.ylabel('Frequency')
plt.legend(title='Funding Type')
st.pyplot(plt)

#################### MONTHS FROM FOUNDING TO MOST RECENT FUNDING ROUND ############################

# Set the style
plt.style.use('fivethirtyeight')

# Filter out rows with NaN values in 'Months Since Founding' and non-negative months
df_filtered = df_final.dropna(subset=['months_since_founded'])
df_filtered = df_filtered[df_filtered['months_since_founded'] >= 0]

# List of rounds to consider
considered_rounds = ['Pre-Seed', 'Seed', 'Series A', 'Series B', 'Series C', 'Series D', 'Series E']
df_filtered['funding_category'] = df_filtered['last_funding_type'].apply(lambda x: x if x in considered_rounds else np.nan)
df_filtered = df_filtered.dropna(subset=['funding_category'])

# Define a hypothetical company
hypothetical_company = {
    'funding_category': 'Series B',
    'Months Since Founding': 45
}

# Create a KDE plot
plt.figure(figsize=(12, 8))

total_companies = len(df_filtered)
y_text_positions = np.linspace(0.1, 0.9, len(considered_rounds))

# Dictionary to store KDE data for interpolation
kde_data = {}

for i, round in enumerate(considered_rounds):
    subset = df_filtered[df_filtered['funding_category'] == round]['months_since_founded']
    kde = sns.kdeplot(subset, label=round, linestyle='-', linewidth=1.5 if round == hypothetical_company['funding_category'] else 1, fill=True if round == hypothetical_company['funding_category'] else False, alpha=0.5 if round == hypothetical_company['funding_category'] else 0.3)

    # Store KDE data
    kde_x, kde_y = kde.get_lines()[-1].get_data()
    kde_data[round] = (kde_x, kde_y)

    # Median line
    median_value = subset.median()
    plt.axvline(median_value, linestyle='dotted', linewidth=1, color='grey')
    plt.text(median_value, plt.ylim()[1] * y_text_positions[i], f'{round}: {int(median_value)} mos.', rotation=15, ha='right', va='center', fontsize=10, color='grey')

# Highlight hypothetical company
kde_values = sns.kdeplot(df_filtered[df_filtered['funding_category'] == hypothetical_company['funding_category']]['months_since_founded']).get_lines()[-1].get_data()
kde_values_y = np.interp(hypothetical_company['Months Since Founding'], kde_values[0], kde_values[1])
plt.scatter(hypothetical_company['Months Since Founding'], kde_values_y, color='red', s=100, zorder=5)
plt.text(hypothetical_company['Months Since Founding'], kde_values_y * 1.06, '  Your Company', color='red', fontsize=12, rotation=15, ha='left', va='center')

# Adjust y-axis to represent the number of companies in increments of 5 from 0 to 40
max_companies = 45
plt.ylim(0, max_companies / total_companies)
y_ticks = np.arange(0, max_companies + 5, 5)
plt.gca().set_yticks(y_ticks / total_companies)
plt.gca().set_yticklabels([f'{int(tick)}' for tick in y_ticks])

# Labels and title
plt.xlabel('Months since Founding')
plt.ylabel('Number of Companies')
plt.title(f'Months from Founding to Most Recent Funding Round - {hypothetical_company["funding_category"]}')
# Remove the legend as requested
plt.legend().remove()

st.pyplot(plt)


################################## Total Funding Raised By Companies in Series X ################

# Set the style
plt.style.use('fivethirtyeight')

# Convert 'total_funding_usd' column to numeric, forcing errors to NaN, then drop NaNs
df_final['total_funding_usd'] = pd.to_numeric(df_final['total_funding_usd'], errors='coerce')
df_funding_filtered = df_final.dropna(subset=['total_funding_usd'])

# Convert the total funding to millions of dollars
df_funding_filtered['total_funding_usd'] = df_funding_filtered['total_funding_usd'] / 1e6

# List of rounds to consider: Series A, Series B, Series C
considered_rounds = ['Series A', 'Series B', 'Series C']
df_funding_filtered['funding_category'] = df_funding_filtered['last_funding_type'].apply(lambda x: x if x in considered_rounds else np.nan)
df_funding_filtered = df_funding_filtered.dropna(subset=['funding_category'])

# Define a hypothetical company
hypothetical_company_funding = {
    'funding_category': 'Series B',
    'total_funding_usd': 50  # Example value in millions
}

# Create the box plot
plt.figure(figsize=(12, 6))

# Draw the box plots
sns.boxplot(x='funding_category', y='total_funding_usd', data=df_funding_filtered,
            order=considered_rounds, palette=["#d3d3d3" if round != hypothetical_company_funding['funding_category'] else "#1f77b4" for round in considered_rounds])

# Highlight the hypothetical company
plt.scatter(hypothetical_company_funding['funding_category'], hypothetical_company_funding['total_funding_usd'], color='red', s=100, zorder=5)
plt.text(hypothetical_company_funding['funding_category'], hypothetical_company_funding['total_funding_usd'] * 1.04, ' Your Company', color='red', fontsize=12, rotation=15, ha='left', va='bottom')

# Set the y-axis limit to 360 million USD
plt.ylim(0, 360)

# Set the labels and title
plt.xlabel('Funding Round')
plt.ylabel('Total Funding (USD in Millions)')
plt.title('Total Funding Raised by Companies in Series B')

st.pyplot(plt)


############################ Funding vs. No. of Employees for Series B Companies ###############

# Define a function to convert employee range to midpoint
def convert_employee_range(employee_range):
    if pd.isna(employee_range):
        return np.nan
    if employee_range == '1-10':
        return 5.5
    elif employee_range == '11-50':
        return 30.5
    elif employee_range == '51-100':
        return 75.5
    elif employee_range == '101-250':
        return 175.5
    elif employee_range == '251-500':
        return 375.5
    elif employee_range == '501-1000':
        return 750.5
    elif employee_range == '1001-5000':
        return 3000.5
    elif employee_range == '5001-10000':
        return 7500.5
    elif employee_range == '10001+':
        return 15000.5
    else:
        return np.nan

# Apply the conversion function
df_final['Number of Employees'] = df_final['Number of Employees'].apply(convert_employee_range)

# Filter for the specified funding round: Series B before any other filtering
funding_round = 'Series B'
df_series_b = df_final[df_final['last_funding_type'] == funding_round]

# Convert relevant columns to numeric, forcing errors to NaN
df_series_b['total_funding_usd'] = pd.to_numeric(df_series_b['total_funding_usd'], errors='coerce')
df_series_b['Number of Employees'] = pd.to_numeric(df_series_b['Number of Employees'], errors='coerce')

# Drop NaNs and 0 values
df_series_b_filtered = df_series_b.dropna(subset=['total_funding_usd', 'Number of Employees'])
df_series_b_filtered = df_series_b_filtered[(df_series_b_filtered['total_funding_usd'] > 0) & (df_series_b_filtered['Number of Employees'] > 0)]

# Convert total funding to millions of dollars
df_series_b_filtered['total_funding_usd'] = df_series_b_filtered['total_funding_usd'] / 1e6

# Cap the total funding at 200 million and the number of employees at 400
df_series_b_filtered = df_series_b_filtered[(df_series_b_filtered['total_funding_usd'] <= 200) & (df_series_b_filtered['Number of Employees'] <= 400)]

# Calculate medians for funding and number of employees within the capped data
median_funding = df_series_b_filtered['total_funding_usd'].median()
median_employees = df_series_b_filtered['Number of Employees'].median()

# Define a hypothetical company
hypothetical_company = {
    'total_funding_usd': 50,  # Example value in millions
    'Number of Employees': 150  # Example value
}

# Create the scatterplot
plt.figure(figsize=(12, 6))

# Scatter plot for companies
sns.scatterplot(x='total_funding_usd', y='Number of Employees', data=df_series_b_filtered, color='blue', s=50)

# Plot median lines
plt.axhline(y=median_employees, color='gray', linestyle='--', linewidth=1)
plt.axvline(x=median_funding, color='gray', linestyle='--', linewidth=1)

# Add labels for the median lines
plt.text(median_funding + 1, -45, f'Median Funding: ${median_funding:.1f}M', color='gray', ha='left')
plt.text(-45, median_employees + 5, f'Median Employees: {int(median_employees)}', color='gray', va='bottom')

# Highlight the hypothetical company
plt.scatter(hypothetical_company['total_funding_usd'], hypothetical_company['Number of Employees'], color='red', s=100, zorder=5)
plt.text(hypothetical_company['total_funding_usd'], hypothetical_company['Number of Employees'] + 10, ' Your Company', color='red', fontsize=14, rotation=15, ha='left', va='bottom')

# Set the labels and title
plt.ylabel('Number of Employees')
plt.xlabel('Total Funding (USD in Millions)')
plt.title('Funding vs. No. of Employees for Series B Companies')

# Set limits to ensure the intersection is at the median values and cut off axes at -50
plt.xlim(-50, 200)
plt.ylim(-50, 400)

# Show plot
st.pyplot(plt)

######################### Funding Ratio from One Round to the Next #####################


# Set the style
plt.style.use('fivethirtyeight')

# Assuming df_final is already loaded in your local environment

# Filter for Series B companies
df_series_b = df_final[df_final['last_funding_type'] == 'Series B']

# Define the columns for funding ratios
funding_ratios = ['seed_to_pre_ratio', 'a_to_seed_ratio', 'b_to_a_ratio', 'c_to_b_ratio', 'd_to_c_ratio', 'e_to_d_ratio']

# Melt the dataframe to get all ratios in one column
df_ratios = df_series_b[funding_ratios].melt(var_name='round', value_name='ratio')

# Drop NaN values and zero values
df_ratios = df_ratios.dropna(subset=['ratio'])
df_ratios = df_ratios[df_ratios['ratio'] > 0]

# Calculate the statistics
min_value = df_ratios['ratio'].min()
percentile_25 = df_ratios['ratio'].quantile(0.25)
median_value = df_ratios['ratio'].median()
percentile_75 = df_ratios['ratio'].quantile(0.75)
mean_value = df_ratios['ratio'].mean()
std_dev = df_ratios['ratio'].std()
one_std_dev = mean_value + std_dev
two_std_dev = mean_value + 2 * std_dev

# Define a hypothetical company ratio
hypothetical_ratio = 3.5  # Example value

# Collect all statistics
stats = {
    'Min': min_value,
    '25th Percentile': percentile_25,
    'Median': median_value,
    '75th Percentile': percentile_75,
    'Mean + 1 SD': one_std_dev,
    'Mean + 2 SD': two_std_dev,
    'Your Company': hypothetical_ratio
}

# Print the statistics
#for stat, value in stats.items():
#    print(f'{stat}: {value}')

# Sort the statistics for plotting
sorted_stats = dict(sorted(stats.items(), key=lambda item: item[1]))

# Create the histogram
plt.figure(figsize=(12, 6))
bars = plt.bar(sorted_stats.keys(), sorted_stats.values(), color=['blue' if k != 'Your Company' else 'red' for k in sorted_stats.keys()])

# Add text labels on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10)

# Labels and title
plt.xlabel('Statistics')
plt.ylabel('Funding Ratio')
plt.title('Funding Ratio from One Round to the Next (Series B Companies)')

st.pyplot(plt)



###################### Proportion of Total Funding by Year and Funding Round #################


# Set the style
plt.style.use('fivethirtyeight')

# List of funding rounds in chronological order
funding_rounds = ['Pre-Seed', 'Seed', 'Series A', 'Series B', 'Series C', 'Series D', 'Series E']

# Filter the data to include only the necessary columns and rows
df_filtered = df_final[['last_funding_type', 'last_funding_year', 'total_funding_usd']].dropna()
df_filtered = df_filtered[df_filtered['last_funding_year'].between(2009, 2023)]
df_filtered = df_filtered[df_filtered['last_funding_type'].isin(funding_rounds)]

# Convert total funding to numeric and handle errors
df_filtered['total_funding_usd'] = pd.to_numeric(df_filtered['total_funding_usd'], errors='coerce')

# Group by funding round and year, then sum the total funding
funding_by_year = df_filtered.groupby(['last_funding_year', 'last_funding_type'])['total_funding_usd'].sum().unstack().fillna(0)

# Normalize the funding to proportions for each year
funding_proportions_by_year = funding_by_year.div(funding_by_year.sum(axis=1), axis=0)

# Create the stacked bar plot
plt.figure(figsize=(12, 8))
funding_proportions_by_year.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='viridis', ax=plt.gca())

# Labels and title
plt.xlabel('Year')
plt.ylabel('Proportion of Total Funding')
plt.title('Proportion of Total Funding by Year and Funding Round')

# Add legend
plt.legend(title='Funding Round', bbox_to_anchor=(1.05, 1), loc='upper left')

# Save the figure
#plt.savefig('/Users/andreas/Desktop/03 - Le Wagon/Data ViZ/proportional_funding_by_year.png', dpi=300, bbox_inches='tight')

# Show the figure
st.pyplot(plt)


# Hintergrundbild einfügen
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
