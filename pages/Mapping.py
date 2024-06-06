import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import plotly.express as px
import matplotlib as mpl

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Map 🗺️")

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
tech_software_df = tech_software_df.sort_values(by='Ecosystem_Score', ascending=False).head(80)

# Predefined coordinates for major German cities including new ones
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
    'Bremen': (53.0793, 8.8017),
    'Dresden': (51.0504, 13.7373),
    'Hannover': (52.3759, 9.7320),
    'Nuremberg': (49.4521, 11.0767),
    'Duisburg': (51.4344, 6.7623),
    'Bochum': (51.4818, 7.2162),
    'Wuppertal': (51.2562, 7.1508),
    'Bonn': (50.7374, 7.0982),
    'Bielefeld': (52.0302, 8.5325),
    'Mannheim': (49.4875, 8.4660),
    'Karlsruhe': (49.0069, 8.4037),
    'Münster': (51.9607, 7.6261),
    'Wiesbaden': (50.0826, 8.2400),
    'Augsburg': (48.3705, 10.8978),
    'Aachen': (50.7753, 6.0839),
    'Mönchengladbach': (51.1805, 6.4428),
    'Gelsenkirchen': (51.5177, 7.0857),
    'Braunschweig': (52.2689, 10.5268),
    'Chemnitz': (50.8278, 12.9214),
    'Kiel': (54.3233, 10.1228),
    'Krefeld': (51.3388, 6.5853),
    'Halle (Saale)': (51.4821, 11.9696),
    'Magdeburg': (52.1205, 11.6276),
    'Freiburg im Breisgau': (47.9990, 7.8421),
    'Oberhausen': (51.4963, 6.8638),
    'Lübeck': (53.8655, 10.6866),
    'Erfurt': (50.9848, 11.0299),
    'Rostock': (54.0924, 12.0991),
    'Mainz': (49.9929, 8.2473),
    'Kassel': (51.3127, 9.4797),
    'Hagen': (51.3671, 7.4633),
    'Hamm': (51.6739, 7.8150),
    'Saarbrücken': (49.2402, 6.9969),
    'Mülheim an der Ruhr': (51.4325, 6.8787),
    'Herne': (51.5369, 7.2009),
    'Ludwigshafen am Rhein': (49.4774, 8.4452),
    'Osnabrück': (52.2799, 8.0472),
    'Oldenburg': (53.1435, 8.2146),
    'Leverkusen': (51.0459, 7.0192),
    'Solingen': (51.1652, 7.0671),
    'Potsdam': (52.3906, 13.0645),
    'Neuss': (51.2042, 6.6879),
    'Heidelberg': (49.3988, 8.6724),
    'Paderborn': (51.7189, 8.7575),
    'Darmstadt': (49.8728, 8.6512),
    'Regensburg': (49.0134, 12.1016),
    'Würzburg': (49.7913, 9.9534),
    'Ingolstadt': (48.7665, 11.4257),
    'Heilbronn': (49.1427, 9.2109),
    'Ulm': (48.4011, 9.9876),
    'Wolfsburg': (52.4227, 10.7865),
    'Göttingen': (51.5413, 9.9158),
    'Offenbach am Main': (50.0956, 8.7761),
    'Pforzheim': (48.8922, 8.6946),
    'Recklinghausen': (51.6141, 7.1979),
    'Bottrop': (51.5239, 6.9293),
    'Fürth': (49.4772, 10.9886),
    'Bremerhaven': (53.5396, 8.5809),
    'Reutlingen': (48.4914, 9.2043),
    'Remscheid': (51.1787, 7.1897),
    'Koblenz': (50.3569, 7.5889),
    'Bergisch Gladbach': (50.9856, 7.1326),
    'Erlangen': (49.5897, 11.0078),
    'Moers': (51.4515, 6.6276),
    'Trier': (49.7499, 6.6371),
    'Jena': (50.9271, 11.5892),
    'Siegen': (50.8748, 8.0243),
    'Hildesheim': (52.1508, 9.9511),
    'Salzgitter': (52.1520, 10.3604),
    'Cottbus': (51.7563, 14.3329)
}

# Add coordinates to the dataframe
tech_software_df['Latitude'] = tech_software_df['City'].map(lambda x: city_coordinates.get(x, (np.nan, np.nan))[0])
tech_software_df['Longitude'] = tech_software_df['City'].map(lambda x: city_coordinates.get(x, (np.nan, np.nan))[1])

# Drop rows with NaN coordinates
tech_software_df = tech_software_df.dropna(subset=['Latitude', 'Longitude'])

# Normalize the ecosystem scores for the circle radius
min_score = tech_software_df['Ecosystem_Score'].min()
max_score = tech_software_df['Ecosystem_Score'].max()
tech_software_df['normalized_radius'] = 10 + 80 * (tech_software_df['Ecosystem_Score'] - min_score) / (max_score - min_score)  # Scale between 10 and 30

# Define the custom color map
colors = ['#30a2da', '#98df8a', '#e5ae38','#ff9896', '#fc4f30']
custom_cmap = mpl.colors.LinearSegmentedColormap.from_list("custom_cmap", colors, N=256)

# Create the heatmap with Cartopy
plt.figure(figsize=(10, 8))

# Create a Cartopy map
ax = plt.axes(projection=ccrs.Mercator())
ax.set_extent([5, 15, 47, 55], crs=ccrs.PlateCarree())

# Add coastlines and borders
ax.coastlines(color='white')
ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='white')

# Plot heatmap using scatter plot
sc = ax.scatter(
    tech_software_df['Longitude'],
    tech_software_df['Latitude'],
    s=tech_software_df['normalized_radius']*10,
    c=tech_software_df['Ecosystem_Score'],
    cmap=custom_cmap,
    alpha=0.8,
    edgecolors='w',
    linewidth=0.5,
    transform=ccrs.PlateCarree()
)

# Add a colorbar
cbar = plt.colorbar(sc, ax=ax, orientation='vertical', label='Ecosystem Score')
cbar.set_ticks([0, 2, 4, 6, 8, 10])
cbar.set_ticklabels(['0', '2', '4', '6', '8', '10'])
cbar.ax.tick_params(labelsize=12, colors='white')
cbar.outline.set_edgecolor('white')
cbar.set_label('Ecosystem Score', color='white', fontsize=12)

# Add title
plt.title('Top 10 Cities for Energy and Natural Ressources in Germany', color='white', fontsize=15)

# Optionally, add labels for each city
for i, row in tech_software_df.iterrows():
    plt.text(
        row['Longitude'],
        row['Latitude'],
        row['City'],
        fontsize=9,
        ha='right',
        va='top',
        color='white',
        transform=ccrs.PlateCarree()
    )

# Save and show the plot
plt.savefig("tech_software_heatmap_cartopy.png", dpi=300)
st.pyplot(plt)

# Add background image
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
