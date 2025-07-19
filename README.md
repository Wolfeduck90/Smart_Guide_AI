# 🌾 SmartGuide: AI-Powered Farming Insights

SmartGuide is a lightweight, accessible AI tool designed to support farmers in making smarter decisions around **crop selection**, **planting windows**, **irrigation**, and **harvest timing**. By drawing from existing weather, market, and climate datasets, the tool empowers farmers with timely, data-driven insights to help stabilize food security in the face of climate volatility.

---

## ✨ Features

- 📍 Region-aware crop recommendations  
- 🌦️ Weather-based planting and irrigation guidance  
- 📈 Market demand analysis using live price trends  
- 🌍 Climate signal integration for seasonal forecasting  
- 📊 Visual reports that are easy to interpret and act upon

---

## 🚀 Tech Stack

Built using Python and standard open-source libraries:
- `pandas`, `numpy`: Data handling  
- `matplotlib`, `seaborn`: Visualizations  
- `scikit-learn`: Machine learning (Random Forest)  
- `transformers`: AI-powered suggestions (NLP-based)  
- `requests`: Fetching real-time data from APIs (e.g. OpenWeatherMap)

---

## 📁 Project Structure
SmartGuide/ 
│ ├── SmartGuide.ipynb # Main Jupyter notebook 
├── weather_data.csv # Sample weather inputs 
├── market_prices.csv # Sample market trends 
└── README.md # Project overview



---

## 🧠 How It Works

1. Pulls recent weather forecasts and historical climate data
2. Analyzes market price trends and demand signals
3. Uses simple logic and ML to recommend planting, crop types, and timing
4. Visualizes trends for clarity and transparency

Example logic:
```python
if temperature > 25 and rainfall < 400:
    recommend("sorghum")
elif demand['maize'] > supply['maize']:
    recommend("maize")


🌿 Impact & Purpose
SmartGuide is designed for smallholder farmers, agri-cooperatives, and innovators in climate-resilient agriculture. By leveraging publicly available data and simple modeling, the tool democratizes insights typically locked in expensive platforms—helping stabilize yields and build smarter food systems.

📢 Live Demo & GitHub Page
🔗 View the notebook

📌 Future Plans
Soil-based recommendations

Voice assistant for low-literacy users

Community-sourced crop tips & feedback

Integration into Inkululeko platform ecosystem

🙌 Built By
Developed by Dominik Kean for a final academic project with vision toward scalable, community-driven agricultural innovation.

Let’s grow something meaningful.
