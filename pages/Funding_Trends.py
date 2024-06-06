import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df_final = pd.read_csv("raw_data/X_y_data3.csv")

plt.style.use('dark_background')

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Funding Trends 💰📈")



#################### DISTRIBUTION OF MONTHS SINCE FOUNDED BY FUNDING TYPE  ############################

################### DISTRIBUTION OF MONTHS SINCE FOUNDED BY FUNDING TYPE  ############################

# Assuming df_final is already loaded in your local environment

#################### DISTRIBUTION OF MONTHS SINCE FOUNDED BY FUNDING TYPE  ############################

# Assuming df_final is already loaded in your local environment

# Update the 'last_funding_type' column to combine all rounds after Series E into "Private Equity"
df_final['last_funding_type'] = df_final['last_funding_type'].replace(['Series F', 'Series G'], 'Private Equity')

# Filter out rows with invalid or missing values for 'months_since_founded'
df_final = df_final[np.isfinite(df_final['months_since_founded'])]

# Set plot style to dark background
plt.style.use('dark_background')

# Create combined KDE plot for all funding types
plt.figure(figsize=(14, 8))

# Define desired funding types
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

# Set a vibrant color palette
sns.set_palette("bright")

# Highlight specific company data
your_company_funding_type = 'Seed'
your_company_months_since_founded = df_final[(df_final['last_funding_type'] == your_company_funding_type)]['months_since_founded'].quantile(0.4)

# Iterate through each funding type and plot the KDE
for funding_type, short_label in desired_funding_types.items():
    subset = df_final[df_final['last_funding_type'] == funding_type]
    if funding_type == 'Seed':
        sns.kdeplot(subset['months_since_founded'], label=funding_type, shade=True, color='cyan', lw=2.5)
    else:
        sns.kdeplot(subset['months_since_founded'], label=funding_type, shade=True)

    # Calculate and plot the median
    median = subset['months_since_founded'].median()
    plt.axvline(median, linestyle='--', color='white', linewidth=1, label='_nolegend_')
    y_pos = plt.ylim()[1] * (0.9 - 0.1 * list(desired_funding_types.keys()).index(funding_type))
    plt.text(median, y_pos, f'{short_label}: {median:.0f} months', rotation=15, verticalalignment='center', color='white')

# Highlight "Your Company" in the Seed Round
plt.scatter(your_company_months_since_founded, plt.ylim()[1] * 0.5, color='red', s=100, zorder=5, label='Your Company')
plt.text(your_company_months_since_founded, plt.ylim()[1] * 0.55, 'Your Company', color='red', fontsize=20, rotation=15, ha='left', va='bottom', alpha=0.8)

# Customize the grid lines
plt.grid(color='white', linestyle='-', linewidth=0.5, alpha=0.3)

# Customize the legend
legend = plt.legend(title='Funding Type', facecolor='white', edgecolor='white')
legend.get_frame().set_facecolor('black')

# Customize the plot labels and title
plt.title('Startups Lifecycle by Funding Round', color='white')
plt.xlabel('Months Since Founded', color='white')
plt.ylabel('Number of Companies', color='white')
plt.xticks(color='white')
plt.yticks([])  # Remove y-axis ticks

# Display the plot in Streamlit
st.pyplot(plt)



################################## Total Funding Raised By Companies in Series X ################

################################## Total Funding Raised By Companies in Series X ################

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

################################## Total Funding Raised By Companies in Series X ################

# Set the style
plt.style.use('dark_background')

# Convert 'total_funding_usd' column to numeric, forcing errors to NaN, then drop NaNs
df_final['total_funding_usd'] = pd.to_numeric(df_final['total_funding_usd'], errors='coerce')
df_funding_filtered = df_final.dropna(subset=['total_funding_usd'])

# Convert the total funding to millions of dollars
df_funding_filtered['total_funding_usd'] = df_funding_filtered['total_funding_usd'] / 1e6

# List of rounds to consider: Pre-Seed, Seed, Series A
considered_rounds = ['Pre-Seed', 'Seed', 'Series A']
df_funding_filtered['funding_category'] = df_funding_filtered['last_funding_type'].apply(lambda x: x if x in considered_rounds else np.nan)
df_funding_filtered = df_funding_filtered.dropna(subset=['funding_category'])

# Define a hypothetical company in the Seed round at the 40th percentile
your_company_percentile = 0.4
your_company_funding_category = 'Seed'
your_company_total_funding = df_funding_filtered[df_funding_filtered['funding_category'] == your_company_funding_category]['total_funding_usd'].quantile(your_company_percentile)

# Create the box plot
plt.figure(figsize=(12, 6))

# Define the custom color palette with transparency
colors = {
    'Pre-Seed': '#ff989680',  # Other color
    'Seed': '#98df8a80',      # Color for 'Your Company'
    'Series A': '#ff989680'   # Other color
}

# Draw the box plots
box_plot = sns.boxplot(x='funding_category', y='total_funding_usd', data=df_funding_filtered,
                       order=considered_rounds, palette=colors,
                       flierprops={'markerfacecolor':'#ffffff80', 'markeredgecolor':'#ffffff80'},  # Lighten the outliers
                       linewidth=1.2)  # Lighten the lines around the boxes

# Adjust the transparency of the boxes
for patch in box_plot.artists:
    r, g, b, _ = patch.get_facecolor()
    patch.set_facecolor((r, g, b, 0.5))  # Set alpha to 0.5 for transparency

# Highlight the hypothetical company
plt.scatter(your_company_funding_category, your_company_total_funding, color='red', s=100, zorder=5, alpha=0.8)
plt.text(your_company_funding_category, your_company_total_funding * 2.1, ' Your Company', color='red', fontsize=20, rotation=15, ha='left', va='bottom', alpha=0.8)

# Set the y-axis limit
plt.ylim(0, df_funding_filtered['total_funding_usd'].max() * 0.1)

# Customize the grid lines to be slightly dimmer but still visible
plt.grid(color='white', linestyle='-', linewidth=0.5, alpha=0.5)

# Set the labels and title
plt.xlabel('Funding Round')
plt.ylabel('Total Funding (USD in Millions)')
plt.title('Total Funding Raised by Companies in Pre-Seed, Seed, and Series A')

# Show the figure in Streamlit
st.pyplot(plt)


######################### Funding Ratio from One Round to the Next #####################

######################### Funding Ratio from One Round to the Next #####################

# Set the style
plt.style.use('dark_background')

# Assuming df_final is already loaded in your local environment

# Filter for Seed Round companies
df_seed = df_final[df_final['last_funding_type'] == 'Seed']

# Define the columns for funding ratios
funding_ratios = ['seed_to_pre_ratio', 'a_to_seed_ratio', 'b_to_a_ratio', 'c_to_b_ratio', 'd_to_c_ratio', 'e_to_d_ratio']

# Melt the dataframe to get all ratios in one column
df_ratios = df_seed[funding_ratios].melt(var_name='round', value_name='ratio')

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

# Define a hypothetical company ratio at the 40th percentile
hypothetical_ratio = df_ratios['ratio'].quantile(0.4)  # Example value

# Collect all statistics
stats = {
    'Min': min_value,
    '25th %': percentile_25,
    'Median': median_value,
    '75th %': percentile_75,
    'Mean + 1 SD': one_std_dev,
    'Mean + 2 SD': two_std_dev,
    'Your Company': hypothetical_ratio
}

# Sort the statistics for plotting
sorted_stats = dict(sorted(stats.items(), key=lambda item: item[1]))

# Create the histogram
plt.figure(figsize=(12, 6))

# Define the colors
company_color = '#98df8a80'  # Color for 'Your Company'
other_color = '#ff989680'    # Color for all other statistics
highlight_color = 'red'      # Color for highlighting "Your Company"

bars = plt.bar(sorted_stats.keys(), sorted_stats.values(),
               color=[company_color if k == 'Your Company' else other_color for k in sorted_stats.keys()],
               edgecolor=[highlight_color if k == 'Your Company' else '#ffffff40' for k in sorted_stats.keys()])  # Adjust the edge color for better visibility

# Add text labels on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10)

# Labels and title
plt.ylabel('Funding Ratio')
plt.title('Funding Ratio from One Round to the Next (Seed Round Companies)')

# Make the grid lines fainter
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.3)

# Show the plot in Streamlit
st.pyplot(plt)
