import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

# Assuming df_final is already loaded in your local environment

# Set the style
plt.style.use('fivethirtyeight')

# List of 'has_round' columns in order
has_round_columns = ['has_preseed', 'has_seed', 'has_series_a', 'has_series_b', 'has_series_c', 'has_series_d', 'has_series_e']

# Count the number of 1s in each 'has_round' column, ignoring NaN values
funnel_data = df_final[has_round_columns].sum().reindex(has_round_columns)

# Define colors using the viridis palette
colors = plt.cm.viridis(np.linspace(0, 1, len(funnel_data)))

# Plot the funnel chart
plt.figure(figsize=(10, 8))
ax = plt.gca()

# Define the widths and heights for the bars to create the funnel effect
widths = funnel_data.values
heights = np.diff(np.hstack([widths, 0])) / 2

for i, (width, height) in enumerate(zip(widths, heights)):
    left = -width / 2
    bottom = i - height / 2
    ax.barh(i, width, left=left, height=1, color=colors[i], edgecolor='black')

# Remove the x-ticks
plt.xticks([])

# Set the y-ticks with funding stages
plt.yticks(range(len(has_round_columns)), ['Pre-Seed', 'Seed', 'Series A', 'Series B', 'Series C', 'Series D', 'Series E'])

# Labels and title
plt.xlabel('Number of Companies')
plt.ylabel('Funding Stage')
plt.title('Number of Companies at Each Funding Stage')

# Add value labels to the bars
for i, width in enumerate(widths):
    plt.text(0, i, str(int(width)), va='center', ha='center', color='white', fontsize=12)

# Invert y-axis to have the funnel shape
plt.gca().invert_yaxis()

# Save the figure
#plt.savefig('/Users/andreas/Desktop/03 - Le Wagon/Data ViZ/funnel_chart.png', dpi=300, bbox_inches='tight')

# Define "Your Company" details
your_company_funding_stage = 'has_series_b'
your_company_value = 50  # Example value for your company

# Find the position of "Your Company" in the funnel
your_company_index = has_round_columns.index(your_company_funding_stage)

# Calculate the position to place the marker
width = funnel_data.values[your_company_index]
left = -width / 2
bottom = your_company_index

# Place the marker for "Your Company" slightly off-center to avoid obscuring the label
marker_x_position = width / 4  # One-quarter length of the bar

plt.scatter(marker_x_position, bottom, color='red', s=100, zorder=5)
plt.text(marker_x_position, bottom -0.15, '   Your Company', color='red', fontsize=12, rotation=15, ha='left', va='center')
# Show the figure
st.pyplot(plt)


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
