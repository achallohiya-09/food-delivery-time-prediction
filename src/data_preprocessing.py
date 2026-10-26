"""
data_preprocessing.py
---------------------
Data preprocessing and feature engineering module for the Food Delivery Time Prediction project.
Adheres to strict leakage prevention principles using Scikit-Learn pipelines.
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) using Haversine formula.
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0)**2
    c = 2 * np.arcsin(np.sqrt(np.clip(a, 0, 1)))
    km = 6371.0 * c
    return km


def load_raw_data(filepath=None):
    """Load raw food delivery dataset."""
    if filepath is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(base_dir, "data", "raw", "food_delivery_train.csv")
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    
    df = pd.read_csv(filepath)
    return df


def clean_food_delivery_data(df):
    """
    Clean raw food delivery dataset:
    - Handle string NaN values ('NaN ')
    - Clean target variable 'Time_taken(min)'
    - Impute missing numerical attributes with median
    - Standardize and clean categorical features
    - Engineer 'distance_km' via Haversine calculation
    """
    df = df.copy()

    # Replace string 'NaN ' with true np.nan
    df.replace(to_replace=r'^\s*NaN\s*$', value=np.nan, regex=True, inplace=True)
    df.replace(to_replace=r'^\s*$', value=np.nan, regex=True, inplace=True)

    # 1. Clean Target Variable: 'Time_taken(min)'
    if "Time_taken(min)" in df.columns:
        df["Time_taken(min)"] = df["Time_taken(min)"].astype(str).str.extract(r"(\d+)").astype(float)
        df.dropna(subset=["Time_taken(min)"], inplace=True)
        df["Time_taken(min)"] = df["Time_taken(min)"].astype(int)

    # 2. Clean Delivery Person Age & Ratings
    if "Delivery_person_Age" in df.columns:
        df["Delivery_person_Age"] = pd.to_numeric(df["Delivery_person_Age"], errors="coerce")
        median_age = df["Delivery_person_Age"].median()
        df["Delivery_person_Age"] = df["Delivery_person_Age"].fillna(median_age)

    if "Delivery_person_Ratings" in df.columns:
        df["Delivery_person_Ratings"] = pd.to_numeric(df["Delivery_person_Ratings"], errors="coerce")
        median_rating = df["Delivery_person_Ratings"].median()
        df["Delivery_person_Ratings"] = df["Delivery_person_Ratings"].fillna(median_rating)

    # 3. Clean Coordinates & Engineer Haversine Distance
    coords = ["Restaurant_latitude", "Restaurant_longitude", "Delivery_location_latitude", "Delivery_location_longitude"]
    for col in coords:
        df[col] = pd.to_numeric(df[col], errors="coerce").abs()

    # Filter out or impute unreasonable coordinates (0, 0)
    valid_coords = (
        (df["Restaurant_latitude"] > 5.0) & (df["Restaurant_latitude"] < 40.0) &
        (df["Restaurant_longitude"] > 65.0) & (df["Restaurant_longitude"] < 100.0) &
        (df["Delivery_location_latitude"] > 5.0) & (df["Delivery_location_latitude"] < 40.0) &
        (df["Delivery_location_longitude"] > 65.0) & (df["Delivery_location_longitude"] < 100.0)
    )

    df["distance_km"] = haversine_np(
        df["Restaurant_longitude"], df["Restaurant_latitude"],
        df["Delivery_location_longitude"], df["Delivery_location_latitude"]
    )
    # Replace distance for invalid coordinates with median distance
    median_dist = df.loc[valid_coords, "distance_km"].median()
    if np.isnan(median_dist) or median_dist <= 0:
        median_dist = 9.5
    df.loc[~valid_coords | (df["distance_km"] > 50) | (df["distance_km"] < 0.1), "distance_km"] = median_dist

    # 4. Clean Weather conditions
    if "Weatherconditions" in df.columns:
        df["Weatherconditions"] = df["Weatherconditions"].astype(str).str.replace("conditions ", "", case=False).str.strip()
        df["Weatherconditions"] = df["Weatherconditions"].replace(["nan", "NaN"], "Sunny")

    # 5. Clean Road traffic density
    if "Road_traffic_density" in df.columns:
        df["Road_traffic_density"] = df["Road_traffic_density"].astype(str).str.strip()
        df["Road_traffic_density"] = df["Road_traffic_density"].replace(["nan", "NaN"], "Medium")

    # 6. Clean Type_of_vehicle
    if "Type_of_vehicle" in df.columns:
        df["Type_of_vehicle"] = df["Type_of_vehicle"].astype(str).str.strip().str.lower()

    # 7. Clean multiple_deliveries
    if "multiple_deliveries" in df.columns:
        df["multiple_deliveries"] = pd.to_numeric(df["multiple_deliveries"], errors="coerce")
        df["multiple_deliveries"] = df["multiple_deliveries"].fillna(0).astype(int)

    # 8. Clean Festival
    if "Festival" in df.columns:
        df["Festival"] = df["Festival"].astype(str).str.strip()
        df["Festival"] = df["Festival"].replace(["nan", "NaN"], "No")

    # 9. Clean City
    if "City" in df.columns:
        df["City"] = df["City"].astype(str).str.strip()
        df["City"] = df["City"].replace(["nan", "NaN"], "Metropolitian")

    # 10. Clean Vehicle Condition
    if "Vehicle_condition" in df.columns:
        df["Vehicle_condition"] = pd.to_numeric(df["Vehicle_condition"], errors="coerce").fillna(1).astype(int)

    return df


def get_feature_preprocessor(numeric_features, categorical_features):
    """
    Construct Scikit-Learn ColumnTransformer pipeline:
    - StandardScaler for continuous features
    - OneHotEncoder for nominal categorical features
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features)
        ]
    )
    return preprocessor


def prepare_datasets(df=None, test_size=0.2, random_state=42):
    """
    Full preparation workflow:
    - Cleans data
    - Defines feature sets
    - Splits into train/test
    - Fits preprocessor on X_train only (no leakage)
    - Returns X_train, X_test, y_train, y_test, preprocessor, and feature names
    """
    if df is None:
        raw_df = load_raw_data()
        cleaned_df = clean_food_delivery_data(raw_df)
    else:
        cleaned_df = clean_food_delivery_data(df)

    # Save cleaned data
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    proc_path = os.path.join(base_dir, "data", "processed", "cleaned_food_delivery.csv")
    cleaned_df.to_csv(proc_path, index=False)

    numeric_features = [
        "Delivery_person_Age",
        "Delivery_person_Ratings",
        "distance_km",
        "Vehicle_condition",
        "multiple_deliveries"
    ]

    categorical_features = [
        "Weatherconditions",
        "Road_traffic_density",
        "Type_of_vehicle",
        "Festival",
        "City"
    ]

    target = "Time_taken(min)"

    X = cleaned_df[numeric_features + categorical_features]
    y = cleaned_df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    preprocessor = get_feature_preprocessor(numeric_features, categorical_features)

    return {
        "cleaned_df": cleaned_df,
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "numeric_features": numeric_features,
        "categorical_features": categorical_features,
        "preprocessor": preprocessor
    }


if __name__ == "__main__":
    print("Testing data preprocessing pipeline...")
    data_dict = prepare_datasets()
    print("Cleaned data shape:", data_dict["cleaned_df"].shape)
    print("X_train shape:", data_dict["X_train"].shape)
    print("X_test shape:", data_dict["X_test"].shape)
    print("Data preprocessing passed successfully!")
