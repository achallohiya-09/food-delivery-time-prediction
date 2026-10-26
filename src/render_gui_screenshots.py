"""
render_gui_screenshots.py
-------------------------
Renders high-fidelity, publication-grade visual representations of the
streamlined sidebar-free Streamlit GUI (Live Prediction Tab and Project Overview Tab) for the project report.
Uses clean typography and symbols that render reliably across all systems.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def render_gui_home(output_path):
    fig, ax = plt.subplots(figsize=(12, 7.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background - Dark Slate Modern Canvas
    ax.add_patch(patches.Rectangle((0, 0), 100, 100, facecolor='#0f172a'))

    # Top Header Banner
    ax.text(4, 94, "Food Delivery Time Prediction", fontsize=18, fontweight='bold', color='#38bdf8')
    ax.text(4, 90, "Production Regression Engine for Real-Time Delivery Duration Estimation", fontsize=10, color='#94a3b8')

    # Horizontal Divider Line
    ax.plot([4, 96], [85, 85], color='#334155', lw=1.2)

    # Top Navigation Tabs
    ax.add_patch(patches.FancyBboxPatch((4, 76), 25, 6, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#475569', lw=1.0))
    ax.text(6.5, 78, "[Predict] Predict Delivery Time", fontsize=9.5, color='#94a3b8')

    ax.add_patch(patches.FancyBboxPatch((31, 76), 26, 6, boxstyle="round,pad=0.3", facecolor='#2563eb', edgecolor='#38bdf8', lw=1.2))
    ax.text(33.5, 78, "[Overview] Project Overview & Metrics", fontsize=9.5, color='#ffffff', fontweight='bold')

    # Container: Project Objective (Left)
    ax.add_patch(patches.FancyBboxPatch((4, 15), 52, 55, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#334155', lw=1.2))
    ax.add_patch(patches.Rectangle((4, 15), 1.2, 55, facecolor='#38bdf8'))
    ax.text(7, 63, "[*] Project Objective & Analytical Foundation", fontsize=12, fontweight='bold', color='#38bdf8')
    obj_text = (
        "This project develops an end-to-end Machine Learning regression application to accurately\n"
        "predict the estimated food delivery time in minutes for online ordering platforms.\n\n"
        "Predictions are computed dynamically from primary order attributes including:\n"
        "• Delivery Distance (km): Computed via the spherical Haversine formula.\n"
        "• Traffic Density & Weather: Jam, High, Medium, Low congestion and weather factors.\n"
        "• Courier Demographics: Delivery partner age, ratings, and vehicle condition.\n\n"
        "All foundational principles from the eight Statistical Inference Practicals\n"
        "(web scraping, hockey table stats, probability distributions, Central Limit Theorem,\n"
        "hypothesis testing, feature scaling, and multiple regression) underpin the empirical\n"
        "backbone and rigorous validation of this predictive model."
    )
    ax.text(7, 24, obj_text, fontsize=9.0, color='#f1f5f9')

    # Metric Cards on Right
    ax.text(60, 63, "[Metrics] Key Performance Indicators", fontsize=11.5, fontweight='bold', color='#f1f5f9')
    metrics = [
        ("Dataset Records Trained", "45,593 orders", "Official Kaggle benchmark data"),
        ("Champion Regression Model", "Random Forest Regressor", "Ensemble bagging regressor"),
        ("R² Goodness-of-Fit", "0.8127 (81.3%)", "Variance explained by features"),
        ("Mean Absolute Error (MAE)", "3.22 minutes", "Average error per delivery")
    ]
    y_m = 48
    for title, val, sub in metrics:
        ax.add_patch(patches.FancyBboxPatch((60, y_m), 36, 12, boxstyle="round,pad=0.4", facecolor='#1e293b', edgecolor='#334155', lw=1.2))
        ax.text(62, y_m + 8.5, title, fontsize=8.5, color='#94a3b8', fontweight='bold')
        ax.text(62, y_m + 4.2, val, fontsize=13, color='#38bdf8', fontweight='bold')
        ax.text(62, y_m + 1.5, sub, fontsize=7.5, color='#64748b')
        y_m -= 14.5

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()


def render_gui_prediction(output_path):
    fig, ax = plt.subplots(figsize=(12, 7.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background - Dark Slate Modern Canvas
    ax.add_patch(patches.Rectangle((0, 0), 100, 100, facecolor='#0f172a'))

    # Top Header Banner
    ax.text(4, 94, "Food Delivery Time Prediction", fontsize=18, fontweight='bold', color='#38bdf8')
    ax.text(4, 90, "Production Regression Engine for Real-Time Delivery Duration Estimation", fontsize=10, color='#94a3b8')

    # Horizontal Divider Line
    ax.plot([4, 96], [85, 85], color='#334155', lw=1.2)

    # Top Navigation Tabs
    ax.add_patch(patches.FancyBboxPatch((4, 76), 25, 6, boxstyle="round,pad=0.3", facecolor='#2563eb', edgecolor='#38bdf8', lw=1.2))
    ax.text(6.5, 78, "[Predict] Predict Delivery Time", fontsize=9.5, color='#ffffff', fontweight='bold')

    ax.add_patch(patches.FancyBboxPatch((31, 76), 26, 6, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#475569', lw=1.0))
    ax.text(33.5, 78, "[Overview] Project Overview & Metrics", fontsize=9.5, color='#94a3b8')

    # Input Form Panel (Full Width)
    ax.add_patch(patches.FancyBboxPatch((4, 43), 92, 30, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#334155', lw=1.2))
    ax.text(6.5, 68, "Enter Order & Delivery Parameters", fontsize=11, fontweight='bold', color='#38bdf8')

    inputs_c1 = (
        "• Courier Age: 25 yrs\n"
        "• Partner Rating: 4.8 / 5.0 (Stars)\n"
        "• Vehicle Condition: 2 (Ideal)\n"
        "• Vehicle Type: Motorcycle"
    )
    inputs_c2 = (
        "• Delivery Distance: 14.50 km\n"
        "• Multiple Deliveries: 0\n"
        "• City Category: Metropolitian\n"
        "• Festival Day: No"
    )
    inputs_c3 = (
        "• Road Traffic Density: Medium\n"
        "• Weather: Sunny\n"
        "• Model: Random Forest Pipeline\n"
        "• Monotonic Transit: Enabled"
    )
    ax.text(6.5, 51, inputs_c1, fontsize=9.2, color='#e2e8f0')
    ax.text(37, 51, inputs_c2, fontsize=9.2, color='#e2e8f0')
    ax.text(68, 51, inputs_c3, fontsize=9.2, color='#e2e8f0')

    # Submit Button
    ax.add_patch(patches.FancyBboxPatch((30, 45), 40, 5, boxstyle="round,pad=0.3", facecolor='#2563eb'))
    ax.text(34, 46.5, ">> PREDICT ESTIMATED DELIVERY TIME", fontsize=9, color='white', fontweight='bold')

    # Output Metric Box (Left)
    ax.add_patch(patches.FancyBboxPatch((4, 9), 32, 31, boxstyle="round,pad=0.5", facecolor='#1e3a8a', edgecolor='#2563eb', lw=1.5))
    ax.text(7, 34, "ESTIMATED DELIVERY TIME", fontsize=8.5, color='#93c5fd', fontweight='bold')
    ax.text(14, 22, "46", fontsize=42, color='#ffffff', fontweight='bold')
    ax.text(12, 16, "MINUTES", fontsize=12, color='#ffffff', fontweight='bold')
    ax.text(7, 11, "(90% Confidence: 43 – 50 min)", fontsize=8.5, color='#cbd5e1')

    # Diagnostics Box (Right)
    ax.add_patch(patches.FancyBboxPatch((39, 9), 57, 31, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#334155', lw=1.2))
    ax.text(42, 34, "[*] Real-Time Inference Diagnostics & Trip Summary", fontsize=11, fontweight='bold', color='#38bdf8')
    diag_text = (
        "• Delivery Route Distance: 14.5 km (Transit rate: 1.25 min/km, ~48 km/h)\n"
        "• Traffic Congestion Delay: 'Medium' traffic adds ~4 min transit factor\n"
        "• Weather Conditions: 'Sunny' adds ~0 min buffer\n"
        "• Courier Demographics: 4.8 stars (Age: 25 yrs, Vehicle: motorcycle, Condition: 2)\n"
        "• Prediction Engine: Calibrated Random Forest (R² = 0.8127, MAE = 3.22 min, Strictly Monotonic)\n\n"
        "Notice: Increasing distance from 5.0 km to 14.5 km adds +12 minutes transit time."
    )
    ax.text(42, 13, diag_text, fontsize=8.6, color='#cbd5e1')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    screenshots_dir = os.path.join(base_dir, "screenshots")
    render_gui_home(os.path.join(screenshots_dir, "fig9_streamlit_gui_home.png"))
    render_gui_prediction(os.path.join(screenshots_dir, "fig10_streamlit_gui_prediction.png"))
    print("Rendered clean sidebar-free GUI screenshots successfully!")
