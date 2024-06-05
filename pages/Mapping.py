import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import plotly.express as px

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Map 🗺️")



######################### Heatmap ###########################################



# Standardize city names in df_final
df_final['city'] = df_final['city'].replace({'München': 'Munich', 'Köln': 'Cologne'})

# Define the industry groups (for reference)
industry_groups = [
    'Consumer Goods and Services', 'Health and Biotechnology', 'Industrial and Manufacturing',
    'Technology and Software', 'Government and Military', 'Community and Social Services',
    'Finance and Professional Services', 'Miscellaneous', 'Media and Entertainment'
]

# Group by city and industry and count the number of companies
industry_city_counts = df_final.groupby(['city', 'industry_groups']).size().reset_index(name='count')

# Initialize a dictionary to store ecosystem scores
ecosystem_scores = {}

# Calculate the ecosystem score for each industry
for industry in industry_groups:
    # Filter data for the current industry
    industry_data = industry_city_counts[industry_city_counts['industry_groups'] == industry]

    # Sort by count and select top 20 cities
    top_cities = industry_data.sort_values(by='count', ascending=False).head(20)

    # Calculate the percentile rank
    top_cities['percentile'] = top_cities['count'].rank(pct=True)

    # Convert percentile to ecosystem score (0-10 scale)
    top_cities['ecosystem_score'] = top_cities['percentile'] * 10

    # Store the scores in the dictionary
    for _, row in top_cities.iterrows():
        ecosystem_scores[(row['city'], row['industry_groups'])] = np.round(row['ecosystem_score'], 1)

# Function to get the ecosystem score for a company
def get_ecosystem_score(city, industry):
    return ecosystem_scores.get((city, industry), 0.0)

# Add the ecosystem score to df_final
df_final['ecosystem_score'] = df_final.apply(lambda row: get_ecosystem_score(row['city'], row['industry_groups']), axis=1)

# Filter the top 10 cities for Technology and Software
tech_software_scores = {k: v for k, v in ecosystem_scores.items() if k[1] == 'Technology and Software'}
tech_software_df = pd.DataFrame(list(tech_software_scores.items()), columns=['City_Industry', 'Ecosystem_Score'])
tech_software_df[['City', 'Industry']] = pd.DataFrame(tech_software_df['City_Industry'].tolist(), index=tech_software_df.index)
tech_software_df = tech_software_df.drop(columns=['City_Industry', 'Industry'])
tech_software_df = tech_software_df.sort_values(by='Ecosystem_Score', ascending=False).head(10)

# Predefined coordinates for major German cities
city_coordinates = {
    'Berlin': (52.5200, 13.4050),
    'Hamburg': (53.5511, 9.9937),
    'Munich': (48.1351, 11.5820),
    'Cologne': (50.9375, 6.9603),
    'Frankfurt': (50.1109, 8.6821),
    'Stuttgart': (48.7758, 9.1829),
    'Düsseldorf': (51.2277, 6.7735),
    'Dortmund': (51.5136, 7.4653),
    'Essen': (51.4556, 7.0116),
    'Leipzig': (51.3397, 12.3731),
    # Add more cities as needed
}

# Add coordinates to the dataframe
tech_software_df['Latitude'] = tech_software_df['City'].map(lambda x: city_coordinates.get(x, (np.nan, np.nan))[0])
tech_software_df['Longitude'] = tech_software_df['City'].map(lambda x: city_coordinates.get(x, (np.nan, np.nan))[1])

# Drop rows with NaN coordinates
tech_software_df = tech_software_df.dropna(subset=['Latitude', 'Longitude'])

# Normalize the ecosystem scores for the circle radius
min_score = tech_software_df['Ecosystem_Score'].min()
max_score = tech_software_df['Ecosystem_Score'].max()
tech_software_df['normalized_radius'] = 10 + 20 * (tech_software_df['Ecosystem_Score'] - min_score) / (max_score - min_score)  # Scale between 10 and 30

# Create the heatmap with Cartopy
plt.figure(figsize=(10, 8))

# Create a Cartopy map
ax = plt.axes(projection=ccrs.Mercator())

# Add coastlines and borders
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':')

# Plot heatmap using scatter plot
sc = ax.scatter(
    tech_software_df['Longitude'],
    tech_software_df['Latitude'],
    s=tech_software_df['normalized_radius']*10,
    c=tech_software_df['Ecosystem_Score'],
    cmap='viridis',
    alpha=0.6,
    edgecolors='w',
    linewidth=0.5,
    transform=ccrs.PlateCarree()
)

# Add a colorbar
plt.colorbar(sc, ax=ax, orientation='vertical', label='Ecosystem Score')

# Add title
plt.title('Top 10 Cities for Technology and Software in Germany')

# Optionally, add labels for each city
for i, row in tech_software_df.iterrows():
    plt.text(
        row['Longitude'],
        row['Latitude'],
        row['City'],
        fontsize=9,
        ha='right',
        va='top',
        color='black',
        transform=ccrs.PlateCarree()
    )

# Save and show the plot
plt.savefig("tech_software_heatmap_cartopy.png", dpi=300)
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
