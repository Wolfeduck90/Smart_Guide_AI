import streamlit as st
import pandas as pd
from smartguide_model import ai_crop_recommendation, merged_df

st.title("🌾 SmartGuide - AI Agricultural Advisor")

country = st.text_input("Enter your country")
crop = st.text_input("Enter your crop (e.g., Maize)")
size = st.number_input("Enter your farm size (in acres)", min_value=1)

if st.button("Get Recommendation"):
    subset = merged_df[
        (merged_df['Country'].str.lower() == country.lower()) &
        (merged_df['Crop'].str.lower() == crop.lower())
    ]
    if subset.empty:
        st.warning("No data available for that crop and region.")
    else:
        avg_temp = subset['AverageTemperature'].mean()
        avg_metric = subset['MetricValue'].mean()
        rec = ai_crop_recommendation(country, crop, avg_temp, avg_metric, size)
        st.success(rec)
