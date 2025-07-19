import streamlit as st
import pandas as pd
from smartguide_model import ai_crop_recommendation, merged_df

st.title("🌾 SmartGuide - AI Agricultural Advisor")

# Step 1: Load available countries
available_countries = sorted(merged_df['Country'].dropna().unique())
selected_country = st.selectbox("Select your country:", available_countries)

# Step 2: Filter crop options based on selected country
filtered_crops = sorted(
    merged_df[merged_df['Country'] == selected_country]['Crop'].dropna().unique()
)
selected_crop = st.selectbox("Select a crop grown in your country:", filtered_crops)

# Step 3: Farm size input
farm_size = st.number_input("Enter your farm size (in acres):", min_value=1)

# Step 4: Trigger AI Recommendation
if st.button("Get Recommendation"):
    subset = merged_df[
        (merged_df['Country'] == selected_country) &
        (merged_df['Crop'] == selected_crop)
    ]
    if subset.empty:
        st.warning("No data available for that crop in this country.")
    else:
        avg_temp = subset['AverageTemperature'].mean()
        avg_metric = subset['MetricValue'].mean()
        rec = ai_crop_recommendation(selected_country, selected_crop, avg_temp, avg_metric, farm_size)
        st.success(rec)

