# Lagos Property Price Prediction

A machine learning web app that estimates property prices in Lagos, Nigeria, based on property type, location, and size. Built on real property listing data and deployed as an interactive Streamlit app.

**Live app:** [laghousespricepred.streamlit.app](https://laghousespricepred.streamlit.app/)

---

## Overview

Real estate pricing in Lagos varies enormously by location, property type, and size, and there's no simple public tool to get a quick, data-driven estimate. This project builds a regression model on cleaned property listing data and wraps it in a simple web interface: pick a property type, location, number of bedrooms and bathrooms, and get an estimated price along with a category (Budget / Mid-Range / Luxury).

## Features

- Predicts property price from 4 inputs: property type, location, bedrooms, bathrooms
- Covers 37+ locations across Lagos (Lekki, Ikeja, Victoria Island, Ajah, Yaba, and more)
- Classifies predictions into Budget, Mid-Range, or Luxury categories
- Simple, interactive UI — no technical knowledge needed to use it

## Dataset

The underlying data was collected via custom web scraping across two major Nigerian property platforms, then cleaned and structured into a public dataset — including resolving currency mix-ups, standardizing property categories, and handling extreme outliers.

📊 **[Nigerian Real Estate Rental Market Dataset (Kaggle)](https://www.kaggle.com/datasets/ibenjamean/real-estate-rental-market-dataset-2026)**

## Tech Stack

| Layer | Tools |
|---|---|
| Data cleaning & analysis | pandas, NumPy |
| Modeling | scikit-learn (Pipeline, OneHotEncoder, RandomForestRegressor) |
| Model serialization | joblib |
| Web interface | Streamlit |
| Deployment | Streamlit Community Cloud |

## How It Works

1. **Data cleaning:** Raw property listings were cleaned to handle mixed currency formats, inconsistent location naming, and missing values.
2. **Feature engineering:** Property type and location were encoded using `OneHotEncoder`; bedrooms and bathrooms were used as numeric features.
3. **Modeling:** Several models were compared (Linear Regression, Decision Tree, Random Forest, XGBoost). A `RandomForestRegressor` inside a scikit-learn `Pipeline` was selected as the final model based on cross-validated performance.
4. **Deployment:** The trained pipeline was serialized with `joblib` and served through a Streamlit app, deployed publicly via Streamlit Community Cloud.

## Project Structure

```
├── app.py                          # Streamlit app
├── house_price_model.pkl           # Trained model pipeline (preprocessing + Random Forest)
├── requirements.txt                # Python dependencies
├── modeling.ipynb                  # Model development and evaluation
├── Lagos_Properties.ipynb          # Data cleaning and exploratory analysis
└── Datasets/                       # Raw and cleaned property listing data
```

## Running Locally

Clone the repo and install dependencies:

```bash
git clone https://github.com/meanima/lagos-properties-price-prediction.git
cd lagos-properties-price-prediction
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

## Future Improvements

- Rebuild the frontend with Flask/FastAPI + custom HTML/CSS/JS for more control over the interface
- Expand the dataset with more recent listings for better price accuracy
- Add confidence intervals or price ranges alongside point predictions
- Experiment with gradient boosting models (XGBoost, LightGBM) for potential accuracy gains

## Author

**Benjamin Kadiri**
A personal project exploring end-to-end machine learning deployment — from raw scraped data to a live public app.
