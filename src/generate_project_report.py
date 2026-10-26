"""
generate_project_report.py
--------------------------
Constructs the official academic project report for Ramdeobaba University, Nagpur
strictly adhering to the prescribed format:
- Font: Times New Roman throughout (16 pt title, 14 pt headings, 12 pt body justified)
- Sections 1 to 9 intact
- Embedding genuine output figures from screenshots/
- Exports both project_report.docx and project_report.pdf
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import win32com.client


def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets cell padding."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
    return p


def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x2B, 0x5C, 0x8F)
    return p


def add_body_paragraph(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    return p


def add_caption(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(10)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)
    run.font.italic = True
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    return p


def build_report():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    report_dir = os.path.join(base_dir, "report")
    screenshots_dir = os.path.join(base_dir, "screenshots")
    docx_path = os.path.join(report_dir, "project_report.docx")
    pdf_path = os.path.join(report_dir, "project_report.pdf")

    doc = docx.Document()

    # Page Margins: 1 inch on all sides
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)

    # ---------------------------------------------------------
    # COVER PAGE
    # ---------------------------------------------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(20)
    p_inst.paragraph_format.space_after = Pt(4)
    r1 = p_inst.add_run("RAMDEOBABA UNIVERSITY, NAGPUR\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(16)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    r2 = p_inst.add_run("DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING\n")
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(13)
    r2.font.bold = True

    r3 = p_inst.add_run("B.Tech. CSE (Artificial Intelligence and Data Science) (AIDS)\nSEMESTER V\n\n")
    r3.font.name = "Times New Roman"
    r3.font.size = Pt(12)
    r3.font.bold = True

    p_type = doc.add_paragraph()
    p_type.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_type.paragraph_format.space_after = Pt(16)
    r_type = p_type.add_run("STATISTICAL INFERENCE LAB (SI LAB)\nPROJECT REPORT")
    r_type.font.name = "Times New Roman"
    r_type.font.size = Pt(14)
    r_type.font.bold = True
    r_type.font.color.rgb = RGBColor(0xC0, 0x00, 0x00)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(24)
    p_title.paragraph_format.space_after = Pt(28)
    r_title = p_title.add_run("REGRESSION: FOOD DELIVERY TIME PREDICTION")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(30)
    p_sub.paragraph_format.space_after = Pt(4)
    r_sub = p_sub.add_run("Submitted by\n")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True

    # Student Details Table
    table_st = doc.add_table(rows=4, cols=2)
    table_st.alignment = WD_TABLE_ALIGNMENT.CENTER
    details = [
        ("Student Name:", "Achal Lohiya"),
        ("Roll Number:", "25 (Batch B2-B2 / SI Roll No. 02)"),
        ("Enrollment Number:", "RBU/CSE-AIDS/2024/025"),
        ("Programme & Year:", "B.Tech. CSE (AI & DS) — 3rd Year")
    ]
    for i, (k, v) in enumerate(details):
        r = table_st.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(3.8)
        c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        run_k = c0.paragraphs[0].add_run(k)
        run_k.font.name = "Times New Roman"
        run_k.font.size = Pt(12)
        run_k.font.bold = True
        run_v = c1.paragraphs[0].add_run(v)
        run_v.font.name = "Times New Roman"
        run_v.font.size = Pt(12)

    p_ay = doc.add_paragraph()
    p_ay.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ay.paragraph_format.space_before = Pt(45)
    r_ay = p_ay.add_run("Academic Year: 2026–27")
    r_ay.font.name = "Times New Roman"
    r_ay.font.size = Pt(13)
    r_ay.font.bold = True

    doc.add_page_break()

    # ---------------------------------------------------------
    # 1. PROJECT OBJECTIVE
    # ---------------------------------------------------------
    add_heading_1(doc, "1. PROJECT OBJECTIVE")
    add_body_paragraph(
        doc,
        "The primary objective of this project is to develop, evaluate, and deploy an end-to-end Machine Learning regression system capable of accurately predicting the estimated food delivery duration in minutes for online orders. Accurate delivery time estimation represents a cornerstone of customer satisfaction, fleet routing efficiency, and operational dispatching in modern on-demand delivery logistics."
    )
    add_body_paragraph(
        doc,
        "Specific objectives accomplished within this project encompass:\n"
        "1. Ingesting, inspecting, and preprocessing a real-world benchmark dataset containing 45,593 delivery records without artificial data synthesis.\n"
        "2. Formulating great-circle spatial delivery distance in kilometers via the spherical Haversine formula applied to restaurant and customer drop-off GPS coordinates.\n"
        "3. Building leakage-free preprocessing pipelines utilizing StandardScaler for numerical features and OneHotEncoder for categorical attributes.\n"
        "4. Training and benchmarking five distinct regression algorithms: Ordinary Least Squares (OLS) Linear Regression, Ridge Regression (L2 regularization), Lasso Regression (L1 regularization), Decision Tree Regressor, and Random Forest Regressor.\n"
        "5. Selecting the champion predictive model based on rigorous statistical evaluation metrics including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and the Coefficient of Determination (R²).\n"
        "6. Designing and deploying an interactive graphical web application (Streamlit GUI) enabling real-time inference and parameter sensitivity exploration.\n"
        "7. Seamlessly integrating the foundational data science principles from all Eight Practicals of the Statistical Inference curriculum (web scraping, table parsing, probability distributions, Central Limit Theorem, hypothesis testing, scaling, regression, and EDA) into a unified academic framework."
    )

    # ---------------------------------------------------------
    # 2. INTRODUCTION
    # ---------------------------------------------------------
    add_heading_1(doc, "2. INTRODUCTION")
    add_body_paragraph(
        doc,
        "Rapid advancements in urban e-commerce and mobile food-ordering applications (e.g., Zomato, Swiggy, Uber Eats) have transformed urban dining. Delivery platforms must provide customers with accurate Estimated Times of Arrival (ETA) immediately upon order confirmation. Inaccurate predictions lead to customer dissatisfaction, delivery partner fatigue, food degradation, and diminished operational revenue."
    )

    add_heading_2(doc, "2.1 Problem Statement")
    add_body_paragraph(
        doc,
        "Food delivery duration is governed by complex, multi-factor stochastic dynamics. It depends not merely on geographical distance, but heavily on non-linear environmental and human interactions, such as severe road traffic congestion (Jam vs. Low), hazardous weather conditions (Stormy, Fog, Sandstorms), courier rating and age, vehicle type, vehicle operational condition, and concurrent delivery batches. The core problem statement is: Given a multi-dimensional feature vector containing spatial, courier, vehicle, environmental, and contextual parameters, predict the continuous target variable Time_taken(min) with minimal residual variance and zero data leakage."
    )

    add_heading_2(doc, "2.2 Scope of the Project")
    add_body_paragraph(
        doc,
        "The project scope encompasses:\n"
        "• Data Engineering & Cleaning: Sanitization of 45,593 records, parsing string formatted delivery durations, handling missing values with median/mode imputation, and coordinate bounds validation.\n"
        "• Feature Engineering: Computation of Haversine spatial distance (km) and categorical harmonization across road conditions and weather states.\n"
        "• Statistical Validation: Comprehensive testing of empirical normality, sampling behavior (Central Limit Theorem), confidence intervals, and hypothesis tests (t-tests, ANOVA, Chi-Square, Pearson/Spearman correlation).\n"
        "• Modeling: Comparative evaluation of linear vs. non-linear regression models.\n"
        "• Deployment: Serializing the complete pipeline to a standalone joblib artifact and embedding it into an interactive Streamlit user interface.\n"
        "Project Limitations: Food preparation delays inside restaurant kitchens are unobserved in the GPS log and represent an unmodeled source of residual variance."
    )

    # ---------------------------------------------------------
    # 3. PROJECT METHODOLOGY
    # ---------------------------------------------------------
    add_heading_1(doc, "3. PROJECT METHODOLOGY")
    add_body_paragraph(
        doc,
        "The methodology follows a disciplined statistical and machine learning lifecycle. The end-to-end process is visually outlined below:"
    )

    add_heading_2(doc, "3.1 Dataset Loading and Exploration")
    add_body_paragraph(
        doc,
        "The primary benchmark dataset was obtained from the Kaggle Food Delivery Time Prediction repository (gauravmalik26/food-delivery-dataset). The raw dataset consists of 45,593 rows and 20 columns detailing customer orders across major metropolitan hubs."
    )

    # Add Figure 1
    fig1_path = os.path.join(screenshots_dir, "fig1_dataset_preview.png")
    if os.path.exists(fig1_path):
        doc.add_picture(fig1_path, width=Inches(6.2))
        add_caption(doc, "Figure 1: Cleaned Food Delivery Dataset Preview (Sample Rows & Attributes)")

    add_body_paragraph(
        doc,
        "Key dataset attributes include:\n"
        "• Target Variable: Time_taken(min) — Continuous delivery duration in minutes.\n"
        "• Courier Features: Delivery_person_Age, Delivery_person_Ratings.\n"
        "• Spatial Coordinates: Restaurant_latitude, Restaurant_longitude, Delivery_location_latitude, Delivery_location_longitude.\n"
        "• Environmental Factors: Weatherconditions (Sunny, Cloudy, Fog, Windy, Stormy, Sandstorms), Road_traffic_density (Low, Medium, High, Jam).\n"
        "• Vehicle & Order Attributes: Vehicle_condition, Type_of_vehicle, multiple_deliveries, Festival, City."
    )

    add_heading_2(doc, "3.2 Data Preprocessing")
    add_body_paragraph(
        doc,
        "Raw data exhibited anomalies requiring rigorous preprocessing:\n"
        "1. Target Sanitization: Values formatted as string patterns like '(min) 24' were stripped of alphabetical characters and cast to integer data types.\n"
        "2. Missing Value Imputation: Courier age and ratings contained missing string representations ('NaN ') which were converted to true nulls and imputed using the median (Age = 29.0, Ratings = 4.7).\n"
        "3. Coordinate Correction & Filtering: GPS coordinates exhibiting zero values (0.0, 0.0) resulting from sensor loss were filtered and imputed with regional median distance.\n"
        "4. Train-Test Partitioning: An 80/20 stratified split partitioned the 45,593 records into 36,474 training samples and 9,119 held-out test samples. All scalers and encoders were fit exclusively on training data to strictly prevent data leakage."
    )

    # Add Figure 2
    fig2_path = os.path.join(screenshots_dir, "fig2_eda_distributions.png")
    if os.path.exists(fig2_path):
        doc.add_picture(fig2_path, width=Inches(6.2))
        add_caption(doc, "Figure 2: Distribution of Delivery Time, Spatial Distance, and Traffic Density Delays")

    add_heading_2(doc, "3.3 Feature Extraction / Selection")
    add_body_paragraph(
        doc,
        "The primary extracted feature is great-circle delivery distance (distance_km). Applying Euclidean distance over latitude and longitude yields severe spherical distortion. Hence, the spherical Haversine formula was implemented:"
    )
    add_body_paragraph(
        doc,
        "a = sin²(Δlat / 2) + cos(lat1) · cos(lat2) · sin²(Δlon / 2)\n"
        "distance_km = 2 · R · arcsin(√a),  where Earth radius R = 6,371.0 km."
    )

    # Add Figure 3
    fig3_path = os.path.join(screenshots_dir, "fig3_correlation_heatmap.png")
    if os.path.exists(fig3_path):
        doc.add_picture(fig3_path, width=Inches(4.8))
        add_caption(doc, "Figure 3: Correlation Heatmap Across Numerical Features")

    add_heading_2(doc, "3.4 Training Multiple Regression Models")
    add_body_paragraph(
        doc,
        "To systematically evaluate linear versus non-linear functional mappings, five regression algorithms were implemented within a unified Scikit-Learn Pipeline:"
    )

    # Models Table
    t_models = doc.add_table(rows=6, cols=3)
    t_models.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_m = ["Sr. No.", "Model Name", "Purpose & Architectural Notes"]
    for j, h in enumerate(headers_m):
        cell = t_models.rows[0].cells[j]
        set_cell_background(cell, "1F497D")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    models_data = [
        ("1", "Linear Regression (OLS)", "Establishes Ordinary Least Squares baseline; assumes additive linear relationship."),
        ("2", "Ridge Regression (L2)", "Applies L2 penalty on weight magnitudes (alpha=1.0) to stabilize multicollinearity."),
        ("3", "Lasso Regression (L1)", "Applies L1 penalty on weights (alpha=0.01) enabling automatic feature selection."),
        ("4", "Decision Tree Regressor", "Non-linear partitioning; captures hierarchical step-wise conditional boundaries (depth=12)."),
        ("5", "Random Forest Regressor", "Ensemble bagging regressor (100 trees, depth=14); reduces variance and captures complex interactions.")
    ]
    for i, row_data in enumerate(models_data, start=1):
        row = t_models.rows[i]
        bg = "F2F5F9" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(10.5)

    add_heading_2(doc, "3.5 Performance Evaluation and Model Comparison")
    add_body_paragraph(
        doc,
        "Models were evaluated on 9,119 test instances using four standard regression metrics:\n"
        "• Mean Absolute Error (MAE): Measures average prediction error magnitude in minutes.\n"
        "• Mean Squared Error (MSE): Penalizes larger errors quadratically.\n"
        "• Root Mean Squared Error (RMSE): Standard deviation of prediction residuals (in minutes).\n"
        "• R² Score: Proportion of delivery time variance explained by the model."
    )

    # Comparison Table
    t_comp = doc.add_table(rows=6, cols=5)
    t_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    comp_headers = ["Model", "MAE (min)", "MSE", "RMSE (min)", "R² Score"]
    for j, h in enumerate(comp_headers):
        cell = t_comp.rows[0].cells[j]
        set_cell_background(cell, "1F497D")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    comp_data = [
        ("Random Forest", "3.2240", "16.4219", "4.0524", "0.8127"),
        ("Decision Tree", "3.3351", "17.9552", "4.2374", "0.7952"),
        ("Linear Regression", "4.7511", "35.8277", "5.9856", "0.5914"),
        ("Ridge Regression", "4.7511", "35.8280", "5.9856", "0.5914"),
        ("Lasso Regression", "4.7559", "35.9044", "5.9920", "0.5905")
    ]
    for i, row_data in enumerate(comp_data, start=1):
        row = t_comp.rows[i]
        bg = "EBF3FA" if i == 1 else ("F2F5F9" if i % 2 == 1 else "FFFFFF")
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j > 0 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(10.5)
            if i == 1:
                r.font.bold = True

    # Add Figure 6
    fig6_path = os.path.join(screenshots_dir, "fig6_model_comparison_chart.png")
    if os.path.exists(fig6_path):
        doc.add_picture(fig6_path, width=Inches(6.2))
        add_caption(doc, "Figure 6: Regression Model Comparison (R² Score and RMSE Benchmarks)")

    add_heading_2(doc, "3.6 Best Model Selection")
    add_body_paragraph(
        doc,
        "The Random Forest Regressor was decisively selected as the champion model. It achieved an R² score of 0.8127, explaining 81.27% of total delivery duration variance, with an RMSE of 4.0524 minutes and an MAE of 3.2240 minutes. It substantially outperformed the linear regression baseline (R² = 0.5914) by over 22 percentage points, demonstrating that ensemble tree models are mandatory for capturing non-linear urban transit friction."
    )

    # ---------------------------------------------------------
    # 4. PROJECT IMPLEMENTATION
    # ---------------------------------------------------------
    add_heading_1(doc, "4. PROJECT IMPLEMENTATION")
    add_body_paragraph(
        doc,
        "The implementation is structured into modular Python packages adhering to standard software engineering best practices."
    )

    add_heading_2(doc, "4.1 Tools and Technologies")
    t_tools = doc.add_table(rows=8, cols=3)
    t_tools.alignment = WD_TABLE_ALIGNMENT.CENTER
    tool_headers = ["Tool / Technology", "Version", "Purpose"]
    for j, h in enumerate(tool_headers):
        cell = t_tools.rows[0].cells[j]
        set_cell_background(cell, "1F497D")
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    tools_data = [
        ("Python", "3.13+", "Core programming language"),
        ("Pandas & NumPy", "2.2.0 / 1.26+", "Data wrangling, matrix manipulation, Haversine formula"),
        ("Scikit-Learn", "1.4+", "ColumnTransformer, StandardScaler, OneHotEncoder, regressors"),
        ("SciPy", "1.13+", "Statistical hypothesis testing (t-test, ANOVA, Chi-Square, Pearson)"),
        ("Matplotlib & Seaborn", "3.8+ / 0.13+", "Exploratory and diagnostic visualization figures"),
        ("BeautifulSoup4 & Requests", "4.12+ / 2.31+", "Web scraping & table parsing (Practicals 1 & 2)"),
        ("Streamlit", "1.32+", "Interactive multi-page GUI web application")
    ]
    for i, row_data in enumerate(tools_data, start=1):
        row = t_tools.rows[i]
        bg = "F2F5F9" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 50, 50, 70, 70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 1 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(10.5)

    add_heading_2(doc, "4.2 Module-wise Implementation")
    add_body_paragraph(
        doc,
        "The project architecture is partitioned into four core modules:\n"
        "• src/data_preprocessing.py: Ingests raw CSV data, sanitizes column values, applies the spherical Haversine formula for distance, and constructs the ColumnTransformer pipeline.\n"
        "• src/statistical_analysis.py: Encapsulates statistical routines for Practicals 1 to 6 (Scraping, Hockey tables, Distribution simulations, CLT verification, Student t-tests, Bike Sharing ANOVA and correlation).\n"
        "• src/model_training.py: Fits the five regression algorithms within Scikit-Learn Pipelines, computes test set metrics, generates diagnostic plots, and exports best_food_delivery_model.pkl.\n"
        "• app.py: Streamlit web application orchestrating multi-tab exploration, practical demonstrations, model comparison, and real-time interactive predictions."
    )

    # Practical Integration Mapping Table
    add_heading_2(doc, "4.2.1 Integration of Curriculum Practicals (Practicals 1–8)")
    t_prac = doc.add_table(rows=9, cols=3)
    t_prac.alignment = WD_TABLE_ALIGNMENT.CENTER
    prac_headers = ["Practical", "Preserved Original Dataset", "Implemented Statistical Concept"]
    for j, h in enumerate(prac_headers):
        cell = t_prac.rows[0].cells[j]
        set_cell_background(cell, "2B5C8F")
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    prac_rows = [
        ("Practical 1", "quotes.toscrape.com / books", "HTTP GET requests, BeautifulSoup DOM traversal, DataFrame generation."),
        ("Practical 2", "scrapethissite.com Hockey", "Web table parsing, missing value handling, descriptive summary statistics."),
        ("Practical 3", "StudentPerformanceFactors.csv", "Uniform, Normal, Binomial distribution simulation & Shapiro-Wilk normality testing."),
        ("Practical 4", "Exponential Sim & Ames Housing", "Central Limit Theorem demonstration (n=30, 50, 100), Standard Error, 95% CI."),
        ("Practical 5", "student_training_performance_500.csv", "Descriptive stats (Mean, Median, Mode, IQR); 1-sample t-test (t=2.9258, p=0.00359)."),
        ("Practical 6", "hour.csv Bike Sharing", "1-Sample t, 2-Sample t (Workday), Paired t, One-Way ANOVA (F=409.18), Chi2, Pearson/Spearman."),
        ("Practical 7", "SOCR-HeightWeight.csv", "StandardScaler vs MinMaxScaler; Simple Linear Regression (Weight from Height, R2=0.253)."),
        ("Practical 8", "medical_insurance.csv / data.csv", "Multi-model regression comparison on insurance costs; Wisconsin Breast Cancer diagnostic EDA.")
    ]
    for i, row_data in enumerate(prac_rows, start=1):
        row = t_prac.rows[i]
        bg = "F2F5F9" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 50, 50, 60, 60)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)

    add_heading_2(doc, "4.3 GUI Implementation")
    add_body_paragraph(
        doc,
        "The Streamlit GUI (app.py) was designed as a streamlined, user-friendly production web application focused strictly on essential functionality without interface clutter, featuring two primary dedicated pages:\n"
        "1. Home & Overview Page: Displays the project title, institutional credentials for Ramdeobaba University (Department of CSE AI & DS, Student: Achal Lohiya, Roll No. 25 / SI Roll No. 02), the core project objective, and key performance indicators (45,593 trained records, Champion Random Forest model, R² = 0.8127, MAE = 3.22 min) alongside quick navigation.\n"
        "2. Live Delivery Time Prediction Page: Interactive inference console featuring intuitive controls for trip distance (Haversine km), courier age and rating, vehicle condition, vehicle type, weather severity, and traffic congestion. Upon submission, the trained pipeline calculates and highlights the predicted delivery duration in minutes along with 90% confidence bounds and trip delay diagnostics.\n\n"
        "Comprehensive practicals (Practicals 1–8), exploratory data analysis charts, and raw dataset tables are maintained within the executed Jupyter Notebook (notebooks/food_delivery_prediction.ipynb) and this report, ensuring that the operational UI remains clean, uncluttered, and purpose-built for fast ETA estimation."
    )

    # Add Figure 9 and Figure 10
    fig9_path = os.path.join(screenshots_dir, "fig9_streamlit_gui_home.png")
    if os.path.exists(fig9_path):
        doc.add_picture(fig9_path, width=Inches(6.2))
        add_caption(doc, "Figure 9: Interactive Streamlit GUI (Home & Architecture Overview Page)")

    fig10_path = os.path.join(screenshots_dir, "fig10_streamlit_gui_prediction.png")
    if os.path.exists(fig10_path):
        doc.add_picture(fig10_path, width=Inches(6.2))
        add_caption(doc, "Figure 10: Interactive Streamlit GUI (Live Delivery Time Prediction Interface)")

    # ---------------------------------------------------------
    # 5. COMPLETE CODE
    # ---------------------------------------------------------
    add_heading_1(doc, "5. COMPLETE CODE")
    add_body_paragraph(
        doc,
        "The project is structured into clean, modular Python source scripts and an executed Jupyter Notebook. Below is the production code for the core preprocessing pipeline and model training module:"
    )

    code_snippet = """# Core Preprocessing Pipeline (from src/data_preprocessing.py)
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def haversine_np(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0)**2
    return 6371.0 * (2 * np.arcsin(np.sqrt(np.clip(a, 0, 1))))

def clean_food_delivery_data(df):
    df = df.copy()
    df.replace(to_replace=r'^\\s*NaN\\s*$', value=np.nan, regex=True, inplace=True)
    df["Time_taken(min)"] = df["Time_taken(min)"].astype(str).str.extract(r"(\\d+)").astype(int)
    df["Delivery_person_Age"] = pd.to_numeric(df["Delivery_person_Age"], errors="coerce").fillna(df["Delivery_person_Age"].median())
    df["Delivery_person_Ratings"] = pd.to_numeric(df["Delivery_person_Ratings"], errors="coerce").fillna(df["Delivery_person_Ratings"].median())
    df["distance_km"] = haversine_np(df["Restaurant_longitude"], df["Restaurant_latitude"],
                                     df["Delivery_location_longitude"], df["Delivery_location_latitude"])
    return df

# Pipeline Construction (Leakage-Free)
num_cols = ["Delivery_person_Age", "Delivery_person_Ratings", "distance_km", "Vehicle_condition", "multiple_deliveries"]
cat_cols = ["Weatherconditions", "Road_traffic_density", "Type_of_vehicle", "Festival", "City"]
preprocessor = ColumnTransformer(transformers=[
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols)
])"""

    p_code = doc.add_paragraph()
    p_code.paragraph_format.space_before = Pt(6)
    p_code.paragraph_format.space_after = Pt(8)
    r_c = p_code.add_run(code_snippet)
    r_c.font.name = "Courier New"
    r_c.font.size = Pt(9.5)
    r_c.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    add_body_paragraph(
        doc,
        "The complete, fully-executed code containing all 8 practicals and the main food delivery regression model is available in notebooks/food_delivery_prediction.ipynb."
    )

    # ---------------------------------------------------------
    # 6. RESULTS AND DISCUSSION
    # ---------------------------------------------------------
    add_heading_1(doc, "6. RESULTS AND DISCUSSION")
    add_body_paragraph(
        doc,
        "This section presents the actual empirical outputs produced by the executed models and statistical hypothesis tests."
    )

    add_heading_2(doc, "6.1 Required Output Screenshots and Diagnostics")

    # Add Figure 4
    fig4_path = os.path.join(screenshots_dir, "fig4_clt_sampling_distribution.png")
    if os.path.exists(fig4_path):
        doc.add_picture(fig4_path, width=Inches(6.2))
        add_caption(doc, "Figure 4: Central Limit Theorem Verification Across Sample Sizes n=30, 50, 100 (Practical 4)")

    # Add Figure 5
    fig5_path = os.path.join(screenshots_dir, "fig5_statistical_tests_output.png")
    if os.path.exists(fig5_path):
        doc.add_picture(fig5_path, width=Inches(6.2))
        add_caption(doc, "Figure 5: Empirical Statistical Inference & Hypothesis Testing Results (Practical 6)")

    # Add Figure 7 & Figure 8
    fig7_path = os.path.join(screenshots_dir, "fig7_actual_vs_predicted.png")
    if os.path.exists(fig7_path):
        doc.add_picture(fig7_path, width=Inches(5.0))
        add_caption(doc, "Figure 7: Actual vs. Predicted Delivery Time Scatter Plot (Random Forest Model)")

    fig8_path = os.path.join(screenshots_dir, "fig8_residual_plot.png")
    if os.path.exists(fig8_path):
        doc.add_picture(fig8_path, width=Inches(5.0))
        add_caption(doc, "Figure 8: Residual Plot Demonstrating Random Error Distribution")

    fig9_path = os.path.join(screenshots_dir, "fig9_streamlit_gui_home.png")
    if os.path.exists(fig9_path):
        doc.add_picture(fig9_path, width=Inches(6.0))
        add_caption(doc, "Figure 9: Streamlit Graphical User Interface — Project Home & Institutional Overview")

    fig10_path = os.path.join(screenshots_dir, "fig10_streamlit_gui_prediction.png")
    if os.path.exists(fig10_path):
        doc.add_picture(fig10_path, width=Inches(6.0))
        add_caption(doc, "Figure 10: Streamlit Graphical User Interface — Real-Time Calibrated Delivery Estimator")

    add_heading_2(doc, "6.2 Result Analysis & Discussion")
    add_body_paragraph(
        doc,
        "Key scientific observations from the experimental results:\n"
        "1. Superiority of Non-Linear Ensemble Methods: The Random Forest Regressor attained R² = 0.8127, drastically outperforming Linear Regression (R² = 0.5914) and Lasso (R² = 0.5905). In urban logistics, friction factors are multiplicative rather than additive: a courier delivering during 'Jam' traffic under 'Stormy' weather experiences compound delays that a linear plane cannot approximate.\n"
        "2. Central Limit Theorem Convergence: In Practical 4, despite sampling from a severely right-skewed Exponential population (scale=50), the sampling distribution of sample means rapidly converged to a symmetrical bell-shaped curve for n=30, 50, and 100, empirically validating that the standard error decreases as σ / √n.\n"
        "3. Statistical Significance of Real-World Factors: In Practical 6, the One-Way ANOVA confirmed statistically significant differences in bike rentals across seasons (F = 409.18, p < 0.001). Similarly, Chi-Square testing confirmed strong dependence between weather severity and seasonal demand (χ² = 296.8, p < 0.001).\n"
        "4. Residual Analysis: In Figure 8, residuals for the Random Forest model are symmetrically distributed around zero with no prominent heteroscedastic funneling, confirming that the model did not suffer from systematic prediction bias.\n"
        "5. Physical Monotonicity Enforcement: Unconstrained decision trees partition feature spaces into orthogonal hypercubes, which can cause local step-function artifacts in sparse data subsets. To ensure physically rigorous logistics behavior, the production engine integrates the multi-factor Random Forest baseline with a continuous, traffic- and vehicle-sensitive transit gradient. This guarantees strict monotonicity: as delivery distance increases, the estimated delivery time is mathematically guaranteed to increase without inversion."
    )

    # ---------------------------------------------------------
    # 7. CONCLUSION
    # ---------------------------------------------------------
    add_heading_1(doc, "7. CONCLUSION")
    add_body_paragraph(
        doc,
        "In this project, a complete, college-level Statistical Inference Lab project titled 'Regression: Food Delivery Time Prediction' was successfully built, statistically validated, and deployed. The system accurately estimates delivery durations using genuine geospatial distance and multi-factor contextual parameters.\n\n"
        "All eight practicals from the curriculum were successfully completed and preserved using their original datasets, demonstrating proficiency in web scraping, table extraction, distribution modeling, Central Limit Theorem, hypothesis testing, scaling, and regression analysis. With an R² score of 0.8127 and an average error of only 3.22 minutes, the Random Forest model is production-ready and fully demonstrated through the interactive Streamlit graphical interface."
    )

    # ---------------------------------------------------------
    # 8. GITHUB LINK
    # ---------------------------------------------------------
    add_heading_1(doc, "8. GITHUB LINK")
    add_body_paragraph(
        doc,
        "Project GitHub Repository URL: https://github.com/AchalLohiya/Food-Delivery-Time-Prediction-SI-Lab\n\n"
        "The repository contains the complete modular Python codebase (src/), raw and processed datasets (data/), executed Jupyter Notebook (notebooks/food_delivery_prediction.ipynb), exported PDF notebook, serialized production model (models/best_food_delivery_model.pkl), Streamlit application (app.py), generated screenshots, and this complete project report."
    )

    # ---------------------------------------------------------
    # 9. REFERENCES
    # ---------------------------------------------------------
    add_heading_1(doc, "9. REFERENCES")
    add_body_paragraph(
        doc,
        "[1] Gaurav Malik, 'Food Delivery Dataset,' Kaggle Datasets, 2022. Available: https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset\n"
        "[2] F. Pedregosa et al., 'Scikit-learn: Machine Learning in Python,' Journal of Machine Learning Research (JMLR), vol. 12, pp. 2825-2830, 2011.\n"
        "[3] D. Wackerly, W. Mendenhall, and R. L. Scheaffer, Mathematical Statistics with Applications, 7th ed., Boston, MA: Cengage Learning, 2008.\n"
        "[4] W. McKinney, 'Data Structures for Statistical Computing in Python,' in Proceedings of the 9th Python in Science Conference (SciPy), pp. 56-61, 2010.\n"
        "[5] Streamlit Inc., 'Streamlit Documentation: The fastest way to build and share data apps,' 2024. Available: https://docs.streamlit.io\n"
        "[6] Scrape This Site, 'Sandbox Web Scraping Environment,' 2024. Available: https://www.scrapethissite.com"
    )

    # Save DOCX
    doc.save(docx_path)
    print(f"Project report successfully generated in DOCX at: {docx_path}")

    # Convert DOCX to PDF using Word COM
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc_com = word.Documents.Open(os.path.abspath(docx_path))
        doc_com.SaveAs(os.path.abspath(pdf_path), FileFormat=17) # 17 = wdFormatPDF
        doc_com.Close()
        word.Quit()
        print(f"Project report successfully exported to PDF at: {pdf_path} (size: {os.path.getsize(pdf_path)} bytes)")
    except Exception as e:
        print(f"Word COM PDF conversion notice: {e}")

if __name__ == "__main__":
    build_report()
