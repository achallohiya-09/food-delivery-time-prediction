# Regression: Food Delivery Time Prediction
### Statistical Inference Lab Project Report & Machine Learning Application
**Ramdeobaba University (RBU), Nagpur**  
*Department of Computer Science and Engineering*  
*B.Tech. CSE (Artificial Intelligence & Data Science) — Semester V*  
**Academic Year:** 2026–27  
**Student Name:** Achal Lohiya  
**Roll No.:** 25 (Batch B2-B2 / SI Lab Roll: 02)  

---

## 📖 Executive Summary
This repository houses the complete academic and practical deliverable for the **Statistical Inference Lab (SI Lab)** project. The project addresses the real-world operational challenge of estimating **Food Delivery Time in Minutes** using machine learning regression algorithms, geospatial distance calculation, and environmental/contextual parameters.

Crucially, this project synthesizes and preserves the empirical findings of all **Eight Practicals** from the official Statistical Inference Lab curriculum into a unified software architecture and academic report.

---

## 🚀 Key Project Highlights
- **Real Benchmark Dataset:** Trained on 45,593 real-world orders from the Kaggle Food Delivery Dataset.
- **Leakage-Free Preprocessing:** Built strictly using Scikit-Learn `ColumnTransformer` and `Pipeline` architectures (`StandardScaler` + `OneHotEncoder`).
- **Geospatial Feature Engineering:** Great-circle delivery distance computed in kilometers using the spherical **Haversine formula**.
- **Model Benchmarking:** Evaluated 5 regression algorithms:
  - Linear Regression (Ordinary Least Squares)
  - Ridge Regression ($L_2$ Regularization)
  - Lasso Regression ($L_1$ Feature Pruning)
  - Decision Tree Regressor
  - **Random Forest Regressor (Champion Model: $R^2 = 0.8127$, $\text{RMSE} = 4.05\text{ min}$)**
- **Streamlined Production GUI:** Intuitive Streamlit web application (`app.py`) focused strictly on the Home Overview and Live Food Delivery Time Estimator, providing instantaneous predictions, confidence intervals, and trip diagnostics without clutter.
- **Institutional Compliance:** Complete project report generated in editable `.docx` and `.pdf` formats strictly following Ramdeobaba University's formatting guidelines (Times New Roman 16/14/12 pt, justified).

---

## 📊 Empirical Model Performance Benchmark

| Model | MAE (Minutes) | MSE | RMSE (Minutes) | $R^2$ Score | Selection Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Random Forest Regressor** | **3.2240** | **16.4219** | **4.0524** | **0.8127** | 🏆 **Best Model (Selected)** |
| **Decision Tree Regressor** | 3.3351 | 17.9552 | 4.2374 | 0.7952 | Runner-Up |
| **Linear Regression (OLS)** | 4.7511 | 35.8277 | 5.9856 | 0.5914 | Baseline Linear |
| **Ridge Regression ($L_2$)** | 4.7511 | 35.8280 | 5.9856 | 0.5914 | Regularized Linear |
| **Lasso Regression ($L_1$)** | 4.7559 | 35.9044 | 5.9920 | 0.5905 | Regularized Linear |

*Evaluation conducted on 9,119 held-out test records (20% split, `random_state=42`).*

---

## 🧪 Curriculum Practicals Mapping (Practicals 1–8)

| Practical No. | Topic & Preserved Dataset | Methods & Techniques Implemented |
| :--- | :--- | :--- |
| **Practical 1** | Web Scraping (`http://quotes.toscrape.com/`) | HTTP GET requests, response codes, BeautifulSoup DOM parsing (`find()`, `find_all()`), Pandas DataFrame creation. |
| **Practical 2** | Web Table Extraction (Hockey Teams, `scrapethissite.com`) | HTML table extraction, type conversions, summary statistics (mean, median, variance, std, quartiles). |
| **Practical 3** | Distributions (`StudentPerformanceFactors.csv`) | Simulated Uniform, Normal, and Binomial distributions; histograms & KDE; empirical normality testing on exam scores. |
| **Practical 4** | CLT & Sampling (Exponential Population & Ames Housing) | Central Limit Theorem simulation ($n=30, 50, 100$); Standard Error calculation; 95% Confidence Intervals for population means. |
| **Practical 5** | Descriptive Statistics (`student_training_performance_500.csv`) | Mean, Median, Mode, Variance, Std Dev, Range, IQR; 95% CI; One-sample t-test ($H_0: \mu = 65.0$, $t = 2.9258$, $p = 0.00359$, Reject $H_0$). |
| **Practical 6** | Statistical Hypothesis Testing (`hour.csv` Bike Sharing) | 1-Sample t-test ($t=32.18$), Independent 2-Sample t-test ($t=2.45$), Paired t-test ($t=-118.4$), One-Way ANOVA across 4 seasons ($F=409.18$, $p<0.001$), Chi-Square test ($\chi^2=296.8$), Pearson & Spearman correlation. |
| **Practical 7** | Preprocessing, Scaling & Regression (`SOCR-HeightWeight.csv`) | StandardScaler vs MinMaxScaler comparison; Simple Linear Regression ($Weight = 3.083 \times Height - 82.576$, $R^2=0.253$). |
| **Practical 8** | Multi-Regression & Classification EDA (`medical_insurance.csv`, `data.csv`) | Medical Insurance regression comparison (OLS, Ridge, Lasso, Trees, Forest); Wisconsin Breast Cancer diagnostic classification EDA. |

---

## 📁 Repository Directory Structure

```text
food-delivery-time-prediction/
├── data/
│   ├── raw/                                 # Raw benchmark & practical datasets
│   │   ├── food_delivery_train.csv
│   │   ├── medical_insurance.csv
│   │   ├── breast_cancer_data.csv
│   │   ├── student_training_performance_500.csv
│   │   ├── SOCR-HeightWeight.csv
│   │   ├── StudentPerformanceFactors.csv
│   │   ├── Housing.csv
│   │   ├── train.csv
│   │   └── hour.csv
│   └── processed/
│       └── cleaned_food_delivery.csv        # Cleaned dataset with Haversine distance
├── notebooks/
│   ├── food_delivery_prediction.ipynb       # Executed Jupyter Notebook with all outputs
│   ├── food_delivery_prediction.html        # Exported HTML notebook
│   └── food_delivery_prediction.pdf         # Exported PDF notebook (684 KB)
├── src/
│   ├── __init__.py
│   ├── setup_datasets.py                    # Dataset downloader and organiser
│   ├── data_preprocessing.py                # Cleaning, Haversine formula, Scikit-Learn pipelines
│   ├── statistical_analysis.py              # Statistical testing routines (Practicals 1–6)
│   ├── model_training.py                    # 5-model training, evaluation & metrics export
│   └── render_gui_screenshots.py            # Diagnostic figures and GUI renderer
├── models/
│   ├── best_food_delivery_model.pkl         # Serialized Random Forest Pipeline package
│   └── model_metrics.json                   # Numerical comparison results JSON
├── screenshots/                             # Publication-grade figures for report
│   ├── fig1_dataset_preview.png
│   ├── fig2_eda_distributions.png
│   ├── fig3_correlation_heatmap.png
│   ├── fig4_clt_sampling_distribution.png
│   ├── fig5_statistical_tests_output.png
│   ├── fig6_model_comparison_chart.png
│   ├── fig7_actual_vs_predicted.png
│   ├── fig8_residual_plot.png
│   ├── fig9_streamlit_gui_home.png
│   └── fig10_streamlit_gui_prediction.png
├── app.py                                   # Streamlit Interactive Web Application
├── requirements.txt                         # Python dependencies
├── README.md                                # Comprehensive documentation & viva guide
└── report/
    ├── project_report.docx                  # RBU Official Formatted Word Report
    └── project_report.pdf                   # RBU Official PDF Report
```

---

## 💻 Installation & Execution Instructions

### 1. Clone or Open the Repository
```bash
git clone https://github.com/your-username/food-delivery-time-prediction.git
cd food-delivery-time-prediction
```

### 2. Set Up a Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run Data Preprocessing and Model Training
```bash
python src/data_preprocessing.py
python src/model_training.py
```

### 4. Launch the Interactive Streamlit GUI
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to interact with the application.

### 5. Open and Run the Jupyter Notebook
```bash
jupyter notebook notebooks/food_delivery_prediction.ipynb
```

---

## 🎓 Viva Voce Preparation Guide (Key Questions & Answers)

1. **Why is Random Forest superior to Linear Regression for delivery prediction?**  
   *Answer:* Linear regression assumes a strictly additive linear relationship ($y = \sum w_i x_i + b$). However, delivery duration involves complex non-linear interactions — for instance, severe traffic delays compound dramatically during stormy weather, which cannot be captured without non-linear splits. Random Forest constructs an ensemble of de-correlated decision trees, achieving $R^2 = 0.8127$ versus $0.5914$ for OLS.

2. **How was delivery distance calculated from latitude and longitude?**  
   *Answer:* Earth is an oblate spheroid, so Euclidean distance is invalid over geographical coordinates. We used the **Haversine formula**, which computes great-circle distance based on spherical trigonometry:
   $$\Delta\sigma = 2 \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$
   Multiplying $\Delta\sigma$ by Earth's mean radius ($R = 6371.0\text{ km}$) yields distance in kilometers.

3. **How did you prevent data leakage during preprocessing?**  
   *Answer:* The train-test split was executed prior to fitting transformers. Both `StandardScaler` and `OneHotEncoder` were encapsulated inside a Scikit-Learn `Pipeline`. Transformers were fitted strictly on `X_train` using `fit_transform()`, and applied to `X_test` using `transform()` only.

4. **What does an $R^2$ score of 0.8127 mean?**  
   *Answer:* $R^2$ represents the coefficient of determination: $1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$. A score of $0.8127$ means that $81.27\%$ of the variance in food delivery times is explained by the model's features (distance, weather, traffic, courier ratings, vehicle condition).

---

## 📜 References
1. **Dataset Source:** Kaggle Food Delivery Time Prediction Dataset by Gaurav Malik (`gauravmalik26/food-delivery-dataset`).
2. **Scikit-Learn Documentation:** Pedregosa et al., *Scikit-learn: Machine Learning in Python*, JMLR 12, pp. 2825-2830, 2011.
3. **Statistical Inference & CLT:** Wackerly, D., Mendenhall, W., & Scheaffer, R. L., *Mathematical Statistics with Applications*, Cengage Learning.
4. **Streamlit Framework:** Streamlit Open-Source Python Library documentation (`https://docs.streamlit.io`).
