import streamlit as st
import pandas as pd
import numpy as np
import folium
from geopy.geocoders import Nominatim
from folium.plugins import HeatMap

df_final = pd.read_csv("/root/code/mberkancetin/startup-website/raw_data/X_y_data3.csv")

# Einbinden des benutzerdefinierten CSS
with open("/root/code/mberkancetin/startup-website/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Map 🗺️")

# Check if entry values are existent in session state
if 'company_age' in st.session_state and 'funding_stage' in st.session_state and 'industry' in st.session_state and 'funding_amount' in st.session_state and 'number_of_articles' in st.session_state:
    company_age = st.session_state.company_age
    company_region = st.session_state.company_region
    last_funding = st.session_state.last_funding
    founded_date = st.session_state.founded_date
    funding_stage = st.session_state.funding_stage
    industry = st.session_state.industry
    funding_amount = st.session_state.funding_amount
    number_of_articles = st.session_state.number_of_articles

    # Beispielhafte Benchmark-Daten
    benchmark_data = {
        'lat': [37.7749, 40.7128, 34.0522, 51.5074, 48.8566],
        'lon': [-122.4194, -74.0060, -118.2437, -0.1278, 2.3522],
        'City': ['San Francisco', 'New York', 'Los Angeles', 'London', 'Paris'],
        'Investment Amount': [5000000, 7000000, 3000000, 4000000, 6000000]
    }
    benchmark_df = pd.DataFrame(benchmark_data)

    # Eingabewerte als DataFrame
    input_data = {
        'lat': [37.7749],  # Example latitude for the input data
        'lon': [-122.4194],  # Example longitude for the input data
        'City': ['San Francisco'],  # Example city for the input data
        'Investment Amount': [funding_amount]
    }
    input_df = pd.DataFrame(input_data)

    st.write("Your comparison with the industry benchmark")

    # Karte mit den Standorten der Startups
    st.map(benchmark_df)

    # Analyse der geografischen Verteilung der Investitionen
    st.write("Geographical Distribution of Funding")
    st.write(benchmark_df)

    # Identifikation von aufstrebenden Startup-Hubs
    st.write("Rising Startup-Hubs")
    st.write(benchmark_df[benchmark_df['Investment Amount'] > 4000000])

    # Vergleich der Eingabewerte mit den Benchmark-Daten
    st.write("Comparison with Your Data")
    st.write(input_df)

    # Visualisierung der Eingabewerte auf der Karte
    st.map(input_df)

else:
    st.warning("Please enter the required information on the input page")



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

# Get coordinates for the cities
geolocator = Nominatim(user_agent="geoapiExercises")

def get_coordinates(city):
    location = geolocator.geocode(city + ', Germany')
    if location:
        return location.latitude, location.longitude
    else:
        return np.nan, np.nan

tech_software_df['Latitude'], tech_software_df['Longitude'] = zip(*tech_software_df['City'].apply(get_coordinates))

# Drop rows with NaN coordinates
tech_software_df = tech_software_df.dropna(subset=['Latitude', 'Longitude'])

# Normalize the ecosystem scores for the circle radius
min_score = tech_software_df['Ecosystem_Score'].min()
max_score = tech_software_df['Ecosystem_Score'].max()
tech_software_df['normalized_radius'] = 10 + 20 * (tech_software_df['Ecosystem_Score'] - min_score) / (max_score - min_score)  # Scale between 10 and 30

# Create the heat map
m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)  # Coordinates for Germany

# Create a heatmap layer with adjusted radius
heat_data = [
    [row['Latitude'], row['Longitude'], row['normalized_radius']] for index, row in tech_software_df.iterrows()
]

HeatMap(heat_data, radius=20, blur=10, max_zoom=1).add_to(m)

# Add markers with ecosystem scores
for index, row in tech_software_df.iterrows():
    folium.map.Marker(
        location=[row['Latitude'], row['Longitude']],
        icon=folium.DivIcon(html=f"""<div style="font-family: Arial; color: black; font-weight: bold; font-size: 12px; padding: 2px; border-radius: 3px;">{row['Ecosystem_Score']}</div>""")
    ).add_to(m)

# Add a hypothetical "Your Company" marker in the fourth-ranked city
if len(tech_software_df) >= 4:
    your_company_city = tech_software_df.iloc[4]
    folium.Marker(
        location=[your_company_city['Latitude'] + 0.1, your_company_city['Longitude'] + 0.1],
        icon=folium.Icon(color='red', icon='remove-sign'),  # X marker
        popup='Your Company'
    ).add_to(m)

    folium.map.Marker(
        location=[your_company_city['Latitude'] + 0.1, your_company_city['Longitude'] + 0.1],
        icon=folium.DivIcon(html=f"""<div style="font-family: Arial; color: red; font-weight: bold; font-size: 12px; transform: rotate(15deg); white-space: nowrap;">Your Company</div>""")
    ).add_to(m)

# Display the map
m.save("tech_software_heatmap.html")








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
