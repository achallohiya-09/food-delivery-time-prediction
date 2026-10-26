"""
model_training.py
-----------------
Model training, evaluation, and artifact generation module for Food Delivery Time Prediction.
Trains 5 regression models, benchmarks metrics, and saves the production pipeline.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from data_preprocessing import prepare_datasets


def train_and_evaluate_models():
    """
    Train 5 regression algorithms on the food delivery dataset:
    - Linear Regression
    - Ridge Regression
    - Lasso Regression
    - Decision Tree Regressor
    - Random Forest Regressor
    Calculates MAE, MSE, RMSE, and R2.
    Saves the best model and performance plots.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, "models")
    screenshots_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)

    print("Step 1: Preparing datasets...")
    data = prepare_datasets()
    X_train = data["X_train"]
    X_test = data["X_test"]
    y_train = data["y_train"]
    y_test = data["y_test"]
    preprocessor = data["preprocessor"]
    cleaned_df = data["cleaned_df"]

    models_to_train = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Lasso Regression": Lasso(alpha=0.01),
        "Decision Tree": DecisionTreeRegressor(max_depth=12, random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=14, random_state=42, n_jobs=-1)
    }

    metrics_list = []
    trained_pipelines = {}
    predictions_dict = {}

    print("\nStep 2: Training and evaluating regression models...")
    for name, regressor in models_to_train.items():
        print(f"Training {name}...")
        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("regressor", regressor)
        ])

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        metrics_list.append({
            "Model": name,
            "MAE": round(float(mae), 4),
            "MSE": round(float(mse), 4),
            "RMSE": round(float(rmse), 4),
            "R2 Score": round(float(r2), 4)
        })

        trained_pipelines[name] = pipeline
        predictions_dict[name] = y_pred

        print(f"  --> {name}: MAE={mae:.3f}, RMSE={rmse:.3f}, R2={r2:.4f}")

    metrics_df = pd.DataFrame(metrics_list).sort_values(by="R2 Score", ascending=False).reset_index(drop=True)
    print("\nModel Comparison Table:")
    print(metrics_df.to_string(index=False))

    # Identify best model
    best_model_name = metrics_df.iloc[0]["Model"]
    best_pipeline = trained_pipelines[best_model_name]
    best_y_pred = predictions_dict[best_model_name]

    print(f"\nBest Model Selected: {best_model_name} (R2={metrics_df.iloc[0]['R2 Score']})")

    # Step 3: Save Best Model Package
    model_package = {
        "model_name": best_model_name,
        "pipeline": best_pipeline,
        "numeric_features": data["numeric_features"],
        "categorical_features": data["categorical_features"],
        "metrics": metrics_df.to_dict(orient="records")
    }
    joblib_path = os.path.join(models_dir, "best_food_delivery_model.pkl")
    joblib.dump(model_package, joblib_path)
    print(f"Saved best model package to: {joblib_path}")

    # Save metrics JSON
    metrics_json_path = os.path.join(models_dir, "model_metrics.json")
    with open(metrics_json_path, "w") as f:
        json.dump(metrics_df.to_dict(orient="records"), f, indent=4)

    # Step 4: Generate Diagnostic Figures
    print("\nStep 4: Generating visual diagnostic plots...")

    # Plot 1: EDA Distributions
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 3, 1)
    sns.histplot(cleaned_df["Time_taken(min)"], kde=True, color="#2b5c8f", bins=25)
    plt.title("Distribution of Delivery Time (Target)", fontsize=12, fontweight="bold")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Frequency")

    plt.subplot(1, 3, 2)
    sns.histplot(cleaned_df["distance_km"], kde=True, color="#d95f02", bins=25)
    plt.title("Distribution of Delivery Distance", fontsize=12, fontweight="bold")
    plt.xlabel("Distance (km)")
    plt.ylabel("Frequency")

    plt.subplot(1, 3, 3)
    sns.boxplot(data=cleaned_df, x="Road_traffic_density", y="Time_taken(min)", palette="Set2")
    plt.title("Delivery Time by Traffic Density", fontsize=12, fontweight="bold")
    plt.xlabel("Traffic Density")
    plt.ylabel("Time (minutes)")
    plt.tight_layout()
    plt.savefig(os.path.join(screenshots_dir, "fig2_eda_distributions.png"), dpi=300)
    plt.close()

    # Plot 2: Correlation Heatmap
    plt.figure(figsize=(8, 6))
    num_cols = ["Delivery_person_Age", "Delivery_person_Ratings", "distance_km", "Vehicle_condition", "multiple_deliveries", "Time_taken(min)"]
    corr_matrix = cleaned_df[num_cols].corr()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="Blues", cbar=True, square=True)
    plt.title("Correlation Heatmap: Numerical Delivery Features", fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(screenshots_dir, "fig3_correlation_heatmap.png"), dpi=300)
    plt.close()

    # Plot 3: Model Comparison Chart
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.barplot(data=metrics_df, x="Model", y="R2 Score", palette="viridis")
    plt.title("Regression Model Comparison: R² Score (Higher is Better)", fontsize=11, fontweight="bold")
    plt.ylim(0, 1.0)
    plt.xticks(rotation=20)
    for idx, row in metrics_df.iterrows():
        plt.text(idx, row["R2 Score"] + 0.02, f"{row['R2 Score']:.3f}", ha="center", fontsize=9, fontweight="bold")

    plt.subplot(1, 2, 2)
    sns.barplot(data=metrics_df, x="Model", y="RMSE", palette="magma")
    plt.title("Regression Model Comparison: RMSE (Lower is Better)", fontsize=11, fontweight="bold")
    plt.xticks(rotation=20)
    for idx, row in metrics_df.iterrows():
        plt.text(idx, row["RMSE"] + 0.1, f"{row['RMSE']:.2f}", ha="center", fontsize=9, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(screenshots_dir, "fig6_model_comparison_chart.png"), dpi=300)
    plt.close()

    # Plot 4: Actual vs Predicted
    plt.figure(figsize=(7, 6))
    plt.scatter(y_test[:400], best_y_pred[:400], alpha=0.6, color="#1f78b4", edgecolors="w", s=45)
    min_val = min(y_test.min(), best_y_pred.min())
    max_val = max(y_test.max(), best_y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], "r--", lw=2, label="Perfect 45° Line")
    plt.title(f"Actual vs Predicted Delivery Time ({best_model_name})", fontsize=12, fontweight="bold")
    plt.xlabel("Actual Delivery Time (min)")
    plt.ylabel("Predicted Delivery Time (min)")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(screenshots_dir, "fig7_actual_vs_predicted.png"), dpi=300)
    plt.close()

    # Plot 5: Residual Plot
    residuals = y_test - best_y_pred
    plt.figure(figsize=(7, 6))
    plt.scatter(best_y_pred[:400], residuals[:400], alpha=0.6, color="#33a02c", edgecolors="w", s=45)
    plt.axhline(0, color="red", linestyle="--", lw=2)
    plt.title(f"Residual Plot ({best_model_name})", fontsize=12, fontweight="bold")
    plt.xlabel("Predicted Delivery Time (min)")
    plt.ylabel("Residuals (Actual - Predicted)")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(screenshots_dir, "fig8_residual_plot.png"), dpi=300)
    plt.close()

    # Plot 6: Central Limit Theorem Sampling Demonstration
    np.random.seed(42)
    pop = np.random.exponential(scale=50, size=10000)
    plt.figure(figsize=(14, 4))
    plt.subplot(1, 4, 1)
    plt.hist(pop, bins=40, color="#7570b3", density=True)
    plt.title("Population: Skewed Exp(50)", fontsize=10, fontweight="bold")
    
    for i, n in enumerate([30, 50, 100], start=2):
        means = [np.mean(np.random.choice(pop, size=n, replace=True)) for _ in range(1000)]
        plt.subplot(1, 4, i)
        plt.hist(means, bins=30, color="#1b9e77", density=True, alpha=0.8)
        plt.title(f"Sampling Dist (n={n})", fontsize=10, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(screenshots_dir, "fig4_clt_sampling_distribution.png"), dpi=300)
    plt.close()

    print("All diagnostic figures generated and saved in screenshots/ successfully!")
    return metrics_df, best_model_name


if __name__ == "__main__":
    train_and_evaluate_models()
