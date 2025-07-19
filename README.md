# 🌾 SmartGuide: AI-Powered Agricultural Advisor

**SmartGuide** is an interactive decision-support tool designed to help farmers, mentors, and agricultural analysts make data-driven crop recommendations. Built with Python, Streamlit, and real-world datasets, SmartGuide offers personalized insights based on farm size, location, and climate history.

---

## 🚀 Features

- Interactive web interface with dropdowns for country and crop
- AI recommendation engine based on historical temperature and yield data
- Predictive model for estimating expected crop yield
- Modular code design for scalability into mobile apps or APIs

---

## 📂 Data Sources

- [GlobalLandTemperaturesByCountry.csv](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)
- Crop production, agricultural inputs, and market prices datasets
- Local CSVs stored in `/datasets`

---

## 🧠 How It Works

Users select:
- Country
- Crop grown
- Farm size (in acres)

SmartGuide automatically pulls relevant historical climate and crop data, generates an AI-backed recommendation, and predicts expected yield using a machine learning model.

---

## 🛠 Technologies Used

- Python 3.10+
- Streamlit
- Pandas, NumPy, scikit-learn
- Jupyter Notebook (for modeling and prototyping)

---

## ✅ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run smartguide_app.py
