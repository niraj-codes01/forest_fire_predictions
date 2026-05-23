# 🌲 Forest Fire Prediction using Machine Learning

## 📖 Overview
This project predicts the **Fire Weather Index (FWI)** using regression models trained on the Algerian Forest Fire dataset.  
It demonstrates an **end‑to‑end ML workflow**: data preprocessing, feature engineering, model training, evaluation, and deployment with Flask.

---

## ✨ Features
- Cleaned and preprocessed Algerian forest fire dataset (`Algerian_forest_fires_cleaned_dataset.csv`)  
- Feature engineering and correlation analysis  
- Regression models: **Linear, Ridge, Lasso, ElasticNet**  
- Ridge Regression selected as the final model (**R² = 0.98**)  
- Flask web app (`application.py`) for user input and predictions  
- HTML frontend (`templates/home.html`) for interactive use  

---

## 🛠 Tech Stack
- **Python**: pandas, numpy, scikit‑learn, matplotlib, seaborn  
- **Flask**: backend deployment  
- **HTML/CSS**: frontend interface  
- **AWS**: deployment hosting  

---

## 📂 Dataset
The dataset used is the **Algerian Forest Fires dataset**, containing meteorological and fire‑related variables.  
**Features include:** Temperature, RH (Relative Humidity), Wind Speed, Rain, FFMC, DMC, ISI, Classes, Region.  
Target variable: **FWI (Fire Weather Index)**.

---

## ▶️ Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/niraj-codes01/forest_fire_predictions.git
   cd forest_fire_predictions
