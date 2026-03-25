# 🏠 ML Regression – Housing Prices

## 🎯 Project Objective

Build an end-to-end **regression model** to predict housing prices based on property features of the local city i live in, Madrid.

This project is part of my Data & AI portfolio and aims to demonstrate a complete workflow:
from data loading and cleaning to feature engineering, model training, evaluation, and result reporting.

---

## 📊 Dataset

- **Source**: To be defined (e.g. Kaggle – House Prices / Ames Housing)
- **Type**: Tabular data with numerical and categorical features
- **Target**: House sale price

Once the final dataset is chosen, this section will include:
- Number of rows and columns
- Brief description of the main features
- Any relevant preprocessing applied (e.g. removing outliers, handling missing values)

---

## ⚙️ Main Steps

1. **Exploratory Data Analysis (EDA)**
   - Understand distributions, missing values, and outliers  
   - Inspect correlations between features and target

2. **Data Cleaning & Feature Engineering**
   - Handle missing values and inconsistent records  
   - Encode categorical variables (e.g. One-Hot Encoding)  
   - Create useful derived features (e.g. house age, room ratios)

3. **Model Training**
   - Baseline: Linear Regression  
   - Additional models: Random Forest, Gradient Boosting / XGBoost (optional)  

4. **Evaluation**
   - Metrics: MAE, RMSE, R²  
   - Compare models and analyse error distribution  
   - Plot predicted vs actual values

5. **Reporting & Conclusions**
   - Summarise main findings and model performance  
   - Highlight limitations and potential improvements

---

## 🧱 Project Structure

This project follows a standard structure I use for my ML/AI projects:

```text
ml-regresion-housing/
│
├── data/
│   ├── raw/          # original dataset(s)
│   └── processed/    # cleaned / transformed data
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_training.ipynb
│   └── 03_evaluation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py   # cleaning & feature engineering
│   ├── training.py        # model training logic
│   └── evaluation.py      # metrics & plots
│
├── reports/
│   └── figures/           # saved plots (PNG, etc.)
│
├── models/                # trained model artifacts (if stored locally)
│
├── requirements.txt
└── README.md
