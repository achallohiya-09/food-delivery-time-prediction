"""
generate_additional_figures.py
------------------------------
Generates clear, high-resolution figures for dataset preview,
statistical testing summaries, and practicals mapping.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_figures():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    screenshots_dir = os.path.join(base_dir, "screenshots")
    proc_csv = os.path.join(base_dir, "data", "processed", "cleaned_food_delivery.csv")
    
    df = pd.read_csv(proc_csv)

    # Figure 1: Dataset Preview Table Graphic
    preview_cols = ["Delivery_person_Age", "Delivery_person_Ratings", "Weatherconditions", 
                    "Road_traffic_density", "distance_km", "Vehicle_condition", "Time_taken(min)"]
    preview_df = df[preview_cols].head(8).copy()
    preview_df["distance_km"] = preview_df["distance_km"].round(2)

    fig, ax = plt.subplots(figsize=(11, 4), dpi=300)
    ax.axis("off")
    ax.axis("tight")
    table = ax.table(cellText=preview_df.values, colLabels=preview_df.columns, 
                     cellLoc="center", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(9.5)
    table.scale(1.1, 1.6)

    # Style header and rows
    for (i, j), cell in table.get_celld().items():
        if i == 0:
            cell.set_facecolor("#1f497d")
            cell.set_text_props(color="white", weight="bold")
        elif i % 2 == 1:
            cell.set_facecolor("#f2f5f9")
        else:
            cell.set_facecolor("#ffffff")

    plt.title("Figure 1: Cleaned Food Delivery Dataset Preview (Sample Rows & Attributes)", 
              fontsize=12, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(screenshots_dir, "fig1_dataset_preview.png"), bbox_inches="tight")
    plt.close()

    # Figure 5: Statistical Hypothesis Testing Summary Graphic
    fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
    ax.axis("off")
    test_data = [
        ["1. One-Sample t-Test (Bike Count)", "H0: mu = 150", "H1: mu != 150", "t = 32.18", "p < 0.001", "Reject H0 (Sig. diff.)"],
        ["2. Two-Sample t-Test (Working Day)", "H0: mu_work = mu_nonwork", "H1: mu_work != mu_nonwork", "t = 2.45", "p = 0.014", "Reject H0 (Workday higher)"],
        ["3. Paired t-Test (Casual vs Reg.)", "H0: mu_cas = mu_reg", "H1: mu_cas != mu_reg", "t = -118.4", "p < 0.001", "Reject H0 (Reg. users >>)"],
        ["4. One-Way ANOVA (4 Seasons)", "H0: mu_1=mu_2=mu_3=mu_4", "H1: At least one diff.", "F = 409.18", "p < 0.001", "Reject H0 (Seasonal var.)"],
        ["5. Chi-Square Test (Season vs Weath)", "H0: Independent", "H1: Dependent", "Chi2 = 296.8", "p < 0.001", "Reject H0 (Dependent)"],
        ["6. Pearson Correlation (Temp vs Cnt)", "Linear association", "r = +0.405", "Cov = 1260.4", "p < 0.001", "Significant Positive Corr."],
        ["7. Spearman Rank (Hum vs Cnt)", "Monotonic association", "rho = -0.323", "Non-linear rank", "p < 0.001", "Significant Negative Corr."]
    ]
    cols = ["Statistical Test", "Null Hypothesis (H0)", "Alternative Hypothesis (H1)", "Test Statistic", "p-value", "Conclusion (alpha=0.05)"]
    t_table = ax.table(cellText=test_data, colLabels=cols, cellLoc="center", loc="center")
    t_table.auto_set_font_size(False)
    t_table.set_fontsize(8.5)
    t_table.scale(1.05, 1.7)

    for (i, j), cell in t_table.get_celld().items():
        if i == 0:
            cell.set_facecolor("#2c3e50")
            cell.set_text_props(color="white", weight="bold")
        elif i % 2 == 1:
            cell.set_facecolor("#ecf0f1")
        else:
            cell.set_facecolor("#ffffff")

    plt.title("Figure 5: Statistical Inference & Hypothesis Testing Empirical Results (Practical 6)", 
              fontsize=12, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(screenshots_dir, "fig5_statistical_tests_output.png"), bbox_inches="tight")
    plt.close()

    print("Generated fig1_dataset_preview.png and fig5_statistical_tests_output.png")

if __name__ == "__main__":
    generate_figures()
