import pandas as pd

# Load merged dataset (if needed, use the cleaned version from your notebook)
crop_df = pd.read_csv("datasets/crop_production.csv")
temp_df = pd.read_csv("datasets/GlobalLandTemperaturesByCountry.csv")

# Clean and merge
iso_map = {
    'AUS': 'Australia', 'CAN': 'Canada', 'USA': 'United States',
    'ARG': 'Argentina', 'MEX': 'Mexico', 'JPN': 'Japan',
    'KOR': 'South Korea', 'NZL': 'New Zealand', 'TUR': 'Turkey', 'DZA': 'Algeria'
}
crop_df = crop_df.rename(columns={'LOCATION': 'Country', 'SUBJECT': 'Crop', 'TIME': 'Year', 'Value': 'MetricValue'})
crop_df['Country'] = crop_df['Country'].map(iso_map)
crop_df['Year'] = pd.to_numeric(crop_df['Year'], errors='coerce')
crop_clean = crop_df[['Country', 'Year', 'Crop', 'MetricValue']].dropna()

temp_df['Year'] = pd.to_datetime(temp_df['dt'], errors='coerce').dt.year
temp_clean = temp_df[['Country', 'Year', 'AverageTemperature']].dropna()

temp_filtered = temp_clean[
    temp_clean['Country'].isin(crop_clean['Country'].dropna()) &
    (temp_clean['Year'] >= 1980)
]
merged_df = pd.merge(crop_clean, temp_filtered, on=['Country', 'Year'], how='inner')

# Recommendation logic
def ai_crop_recommendation(country, crop, temp, metric, size):
    crop = crop.lower()
    if temp > 28 and metric < 5:
        return f"In {country}, climate is hot and yield is low—recommend switching to sorghum or millet."
    elif metric > 7 and crop in ['maize', 'rice']:
        return f"{crop.title()} is viable in {country} on your {size} acre farm."
    else:
        return f"In {country}, consider mixed cropping or improving soil on your {size} acre farm."
