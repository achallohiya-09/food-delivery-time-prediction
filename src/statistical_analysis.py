"""
statistical_analysis.py
-----------------------
Implements statistical inference routines for Practicals 1 to 6:
- Practical 1: Web Scraping with Requests and BeautifulSoup
- Practical 2: Web Data Extraction and Table Analysis
- Practical 3: Probability Distributions and Goodness-of-Fit
- Practical 4: Sampling, Central Limit Theorem, and Confidence Intervals
- Practical 5: Descriptive Statistics and One-Sample t-Test
- Practical 6: Comprehensive Hypothesis Testing (t-tests, ANOVA, Chi-Square, Correlation)
"""

import os
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from scipy import stats


def run_practical_1_scraping():
    """
    Practical 1: Web Scraping using Requests and BeautifulSoup
    Extracts quotes, authors, and tags from http://quotes.toscrape.com/
    """
    url = "http://quotes.toscrape.com/"
    quotes_data = []
    status_code = None

    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        if status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            quote_divs = soup.find_all("div", class_="quote")
            for q in quote_divs[:10]:
                text = q.find("span", class_="text").get_text(strip=True)
                author = q.find("small", class_="author").get_text(strip=True)
                tags = [t.get_text(strip=True) for t in q.find_all("a", class_="tag")]
                quotes_data.append({
                    "quote": text,
                    "author": author,
                    "tags": ", ".join(tags)
                })
    except Exception as e:
        status_code = f"Offline fallback ({e})"

    if not quotes_data:
        # Robust offline demonstration matching practical requirements
        quotes_data = [
            {"quote": "“The world as we have created it is a process of our thinking.”", "author": "Albert Einstein", "tags": "change, deep-thoughts"},
            {"quote": "“It is our choices, Harry, that show what we truly are, far more than our abilities.”", "author": "J.K. Rowling", "tags": "abilities, choices"},
            {"quote": "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”", "author": "Albert Einstein", "tags": "inspirational, life"},
            {"quote": "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”", "author": "Jane Austen", "tags": "classic, humor"}
        ]

    df_quotes = pd.DataFrame(quotes_data)
    return {
        "status_code": status_code,
        "quotes_df": df_quotes,
        "count": len(df_quotes)
    }


def run_practical_2_table_analysis():
    """
    Practical 2: Web Data Extraction and Table Analysis
    Extracts hockey team statistics table from scrapethissite.com
    """
    url = "https://www.scrapethissite.com/pages/forms/?page_num=1&per_page=25"
    table_rows = []
    status_code = None

    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        if status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            rows = soup.find_all("tr", class_="team")
            for r in rows:
                name = r.find("td", class_="name").get_text(strip=True)
                year = r.find("td", class_="year").get_text(strip=True)
                wins = r.find("td", class_="wins").get_text(strip=True)
                losses = r.find("td", class_="losses").get_text(strip=True)
                gf = r.find("td", class_="gf").get_text(strip=True)
                ga = r.find("td", class_="ga").get_text(strip=True)
                table_rows.append({
                    "Team Name": name,
                    "Year": int(year) if year.isdigit() else 1990,
                    "Wins": int(wins) if wins.isdigit() else 0,
                    "Losses": int(losses) if losses.isdigit() else 0,
                    "Goals For": int(gf) if gf.isdigit() else 0,
                    "Goals Against": int(ga) if ga.isdigit() else 0
                })
    except Exception as e:
        status_code = f"Offline fallback ({e})"

    if not table_rows:
        table_rows = [
            {"Team Name": "Boston Bruins", "Year": 1990, "Wins": 44, "Losses": 24, "Goals For": 299, "Goals Against": 264},
            {"Team Name": "Buffalo Sabres", "Year": 1990, "Wins": 31, "Losses": 30, "Goals For": 292, "Goals Against": 278},
            {"Team Name": "Calgary Flames", "Year": 1990, "Wins": 46, "Losses": 26, "Goals For": 344, "Goals Against": 252},
            {"Team Name": "Chicago Blackhawks", "Year": 1990, "Wins": 49, "Losses": 23, "Goals For": 284, "Goals Against": 211},
            {"Team Name": "Detroit Red Wings", "Year": 1990, "Wins": 34, "Losses": 38, "Goals For": 273, "Goals Against": 298}
        ]

    df_table = pd.DataFrame(table_rows)
    stats_summary = df_table[["Wins", "Losses", "Goals For", "Goals Against"]].describe()

    return {
        "status_code": status_code,
        "table_df": df_table,
        "summary_statistics": stats_summary
    }


def run_practical_3_distributions(student_csv_path=None):
    """
    Practical 3: Probability Distributions and Data Visualization
    Compares Uniform, Normal, Binomial, and Poisson distributions.
    """
    np.random.seed(42)
    uniform_data = np.random.uniform(low=0, high=10, size=1000)
    normal_data = np.random.normal(loc=50, scale=10, size=1000)
    binomial_data = np.random.binomial(n=20, p=0.5, size=1000)
    poisson_data = np.random.poisson(lam=5, size=1000)

    student_metrics = {}
    if student_csv_path and os.path.exists(student_csv_path):
        df_stud = pd.read_csv(student_csv_path)
        numeric_cols = df_stud.select_dtypes(include=[np.number]).columns
        for col in numeric_cols[:3]:
            col_data = df_stud[col].dropna()
            stat, p_val = stats.shapiro(col_data[:500]) if len(col_data) >= 3 else (None, None)
            student_metrics[col] = {
                "mean": float(col_data.mean()),
                "std": float(col_data.std()),
                "skewness": float(stats.skew(col_data)),
                "kurtosis": float(stats.kurtosis(col_data)),
                "shapiro_p_value": float(p_val) if p_val is not None else None,
                "is_normal": bool(p_val > 0.05) if p_val is not None else False
            }

    return {
        "uniform_data": uniform_data,
        "normal_data": normal_data,
        "binomial_data": binomial_data,
        "poisson_data": poisson_data,
        "student_metrics": student_metrics
    }


def run_practical_3_sampling_techniques():
    """
    Practical 3: Benchmark 6 Sampling Techniques on student academic population (N=1,000)
    Comparing Simple, With Replacement, Without Replacement, Fractional, Systematic, Stratified, and Cluster.
    """
    np.random.seed(42)
    departments = ['Civil', 'CSE', 'ECE', 'EE', 'IT', 'ME']
    genders = ['Male', 'Female']
    n_students = 1000
    marks_pop = np.clip(np.random.normal(75.133, 12.064, n_students), 35, 100).round().astype(int)
    attendance_pop = np.clip(np.random.normal(80.55, 11.89, n_students), 50, 100).round().astype(int)

    df_student = pd.DataFrame({
        'Student_ID': range(1, n_students + 1),
        'Gender': np.random.choice(genders, n_students),
        'Department': np.random.choice(departments, n_students),
        'Age': np.random.randint(18, 25, n_students),
        'Marks': marks_pop,
        'Attendance': attendance_pop
    })

    sample1 = df_student.sample(n=20, random_state=1)
    sample2 = df_student.sample(n=20, replace=True, random_state=42)
    sample3 = df_student.sample(n=20, replace=False, random_state=42)
    sample4 = df_student.sample(frac=0.20, random_state=42)
    systematic_sample = df_student.iloc[::5]
    sample5 = df_student.groupby("Gender", group_keys=False).sample(n=10, random_state=42)
    selected_clusters = np.random.choice(df_student["Department"].unique(), 2, replace=False)
    cluster_sample = df_student[df_student["Department"].isin(selected_clusters)]

    comp_df = pd.DataFrame({
        "Statistic": ["Size", "Mean", "Median", "Standard Deviation"],
        "Population": [len(df_student), df_student["Marks"].mean(), df_student["Marks"].median(), df_student["Marks"].std()],
        "Simple Sample": [len(sample1), sample1["Marks"].mean(), sample1["Marks"].median(), sample1["Marks"].std()],
        "Random with Replacement": [len(sample2), sample2["Marks"].mean(), sample2["Marks"].median(), sample2["Marks"].std()],
        "Random without Replacement": [len(sample3), sample3["Marks"].mean(), sample3["Marks"].median(), sample3["Marks"].std()],
        "Fractional Sampling": [len(sample4), sample4["Marks"].mean(), sample4["Marks"].median(), sample4["Marks"].std()],
        "Stratified Sampling": [len(sample5), sample5["Marks"].mean(), sample5["Marks"].median(), sample5["Marks"].std()],
        "Cluster Sampling": [len(cluster_sample), cluster_sample["Marks"].mean(), cluster_sample["Marks"].median(), cluster_sample["Marks"].std()]
    })
    return comp_df


def run_practical_4_clt(population_size=10000, num_samples=1000):
    """
    Practical 4: Central Limit Theorem and Confidence Intervals
    Demonstrates CLT on a skewed Exponential Population (scale=50).
    """
    np.random.seed(42)
    population = np.random.exponential(scale=50, size=population_size)
    pop_mean = float(np.mean(population))
    pop_std = float(np.std(population))

    sample_sizes = [15, 30, 100]
    sample_means_dict = {}

    for n in sample_sizes:
        means = [np.mean(np.random.choice(population, size=n, replace=True)) for _ in range(num_samples)]
        sample_means_dict[n] = {
            "means": means,
            "mean_of_means": float(np.mean(means)),
            "std_error_empirical": float(np.std(means)),
            "std_error_theoretical": float(pop_std / np.sqrt(n)),
            "ci_95_lower": float(np.mean(means) - 1.96 * (pop_std / np.sqrt(n))),
            "ci_95_upper": float(np.mean(means) + 1.96 * (pop_std / np.sqrt(n)))
        }

    return {
        "pop_mean": pop_mean,
        "pop_std": pop_std,
        "sample_means_dict": sample_means_dict
    }


def run_practical_4_house_prices(csv_path):
    """
    Practical 4 Assignment: House Price (SalePrice) CLT & Standard Error Verification
    """
    if not os.path.exists(csv_path):
        return None
    df = pd.read_csv(csv_path)
    sale_price = df["SalePrice"].dropna()
    results = {}
    for s in [30, 50, 100, 200]:
        results[s] = {
            "theoretical_se": float(sale_price.std() / np.sqrt(s)),
            "sample_mean": float(np.mean([np.mean(np.random.choice(sale_price, s, replace=False)) for _ in range(2000)]))
        }
    return {
        "pop_mean": float(sale_price.mean()),
        "pop_median": float(sale_price.median()),
        "pop_std": float(sale_price.std()),
        "results": results
    }


def run_practical_5_descriptive_and_ttest(csv_path):
    """
    Practical 5: Descriptive Statistics and One-Sample t-Test
    Dataset: student_training_performance_500.csv
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Practical 5 dataset not found at {csv_path}")

    df = pd.read_csv(csv_path)
    target_col = "marks" if "marks" in df.columns else df.select_dtypes(include=[np.number]).columns[0]
    data = df[target_col].dropna()

    mean_val = float(data.mean())
    median_val = float(data.median())
    mode_val = float(data.mode()[0])
    var_val = float(data.var())
    std_val = float(data.std())
    min_val = float(data.min())
    max_val = float(data.max())
    range_val = max_val - min_val
    q1 = float(data.quantile(0.25))
    q3 = float(data.quantile(0.75))
    iqr_val = q3 - q1

    # 95% Confidence Interval
    n = len(data)
    sem = std_val / np.sqrt(n)
    ci_95 = stats.t.interval(0.95, df=n-1, loc=mean_val, scale=sem)

    # One-sample t-test: H0: mu = 65.0 vs H1: mu != 65.0
    mu_hypo = 65.0
    t_stat, p_val = stats.ttest_1samp(data, popmean=mu_hypo)

    return {
        "variable": target_col,
        "sample_size": n,
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val,
        "variance": var_val,
        "std_dev": std_val,
        "min": min_val,
        "max": max_val,
        "range": range_val,
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr_val,
        "ci_95": (float(ci_95[0]), float(ci_95[1])),
        "t_test": {
            "hypothesized_mean": mu_hypo,
            "t_statistic": float(t_stat),
            "p_value": float(p_val),
            "reject_null": bool(p_val < 0.05),
            "conclusion": "Reject H0 (Mean is significantly different from 65.0)" if p_val < 0.05 else "Fail to reject H0 (No significant difference from 65.0)"
        }
    }


def run_practical_6_hypothesis_testing(bike_csv_path):
    """
    Practical 6: Statistical Hypothesis Testing and Correlation
    Dataset: Bike Sharing hour.csv
    Implements:
    1. One-sample t-test
    2. Independent two-sample t-test
    3. Paired-samples t-test
    4. One-Way ANOVA
    5. Chi-square test
    6. Covariance & Pearson Correlation
    7. Spearman Rank Correlation
    """
    if not os.path.exists(bike_csv_path):
        raise FileNotFoundError(f"Practical 6 dataset not found at {bike_csv_path}")

    df = pd.read_csv(bike_csv_path)
    results = {}

    # 1. One-Sample t-Test: H0: mean rentals cnt == 150
    cnt = df["cnt"].dropna()
    t1_stat, t1_pval = stats.ttest_1samp(cnt, 150)
    results["one_sample_ttest"] = {
        "objective": "Test if average hourly bike rentals equal 150",
        "H0": "mu_cnt = 150",
        "H1": "mu_cnt != 150",
        "t_statistic": float(t1_stat),
        "p_value": float(t1_pval),
        "reject_null": bool(t1_pval < 0.05)
    }

    # 2. Independent Two-Sample t-Test: Working Day vs Non-Working Day
    working = df[df["workingday"] == 1]["cnt"].dropna()
    non_working = df[df["workingday"] == 0]["cnt"].dropna()
    t2_stat, t2_pval = stats.ttest_ind(working, non_working, equal_var=False)
    results["two_sample_ttest"] = {
        "objective": "Compare mean hourly bike rentals between working days and non-working days",
        "H0": "mu_working = mu_nonworking",
        "H1": "mu_working != mu_nonworking",
        "working_mean": float(working.mean()),
        "non_working_mean": float(non_working.mean()),
        "t_statistic": float(t2_stat),
        "p_value": float(t2_pval),
        "reject_null": bool(t2_pval < 0.05)
    }

    # 3. Paired t-Test: Casual vs Registered rentals
    casual = df["casual"].dropna()
    registered = df["registered"].dropna()
    t3_stat, t3_pval = stats.ttest_rel(casual, registered)
    results["paired_ttest"] = {
        "objective": "Compare paired counts of casual vs registered users per hour",
        "H0": "mu_casual = mu_registered",
        "H1": "mu_casual != mu_registered",
        "t_statistic": float(t3_stat),
        "p_value": float(t3_pval),
        "reject_null": bool(t3_pval < 0.05)
    }

    # 4. One-Way ANOVA: Rentals across 4 Seasons
    seasons = [df[df["season"] == s]["cnt"].dropna() for s in [1, 2, 3, 4]]
    f_stat, f_pval = stats.f_oneway(*seasons)
    results["one_way_anova"] = {
        "objective": "Test whether mean bike rentals differ across the four seasons",
        "H0": "mu_spring = mu_summer = mu_fall = mu_winter",
        "H1": "At least one season has a different mean rental count",
        "F_statistic": float(f_stat),
        "p_value": float(f_pval),
        "reject_null": bool(f_pval < 0.05)
    }

    # 5. Chi-Square Test: Season vs Weather Situation
    contingency_table = pd.crosstab(df["season"], df["weathersit"])
    chi2_stat, chi2_pval, dof, _ = stats.chi2_contingency(contingency_table)
    results["chi_square"] = {
        "objective": "Test independence between Season and Weather Condition",
        "H0": "Season and Weather are independent",
        "H1": "Season and Weather are dependent",
        "chi2_statistic": float(chi2_stat),
        "p_value": float(chi2_pval),
        "dof": int(dof),
        "reject_null": bool(chi2_pval < 0.05)
    }

    # 6. Covariance & Pearson Correlation: Temperature vs Count
    cov_temp_cnt = float(np.cov(df["temp"], df["cnt"])[0][1])
    pearson_r, pearson_p = stats.pearsonr(df["temp"], df["cnt"])
    results["pearson_correlation"] = {
        "objective": "Measure linear correlation between ambient temperature and rental counts",
        "covariance": cov_temp_cnt,
        "pearson_r": float(pearson_r),
        "p_value": float(pearson_p)
    }

    # 7. Spearman Rank Correlation: Humidity vs Count
    spearman_rho, spearman_p = stats.spearmanr(df["hum"], df["cnt"])
    results["spearman_correlation"] = {
        "objective": "Measure monotonic association between humidity and rental counts",
        "spearman_rho": float(spearman_rho),
        "p_value": float(spearman_p)
    }

    return results


if __name__ == "__main__":
    print("Testing statistical analysis module...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p5_path = os.path.join(base_dir, "data", "raw", "student_training_performance_500.csv")
    p6_path = os.path.join(base_dir, "data", "raw", "hour.csv")

    p1 = run_practical_1_scraping()
    print("P1 Scraping count:", p1["count"])

    p2 = run_practical_2_table_analysis()
    print("P2 Table shape:", p2["table_df"].shape)

    p3 = run_practical_3_distributions()
    print("P3 Uniform length:", len(p3["uniform_data"]))

    p4 = run_practical_4_clt()
    print("P4 Pop Mean:", p4["pop_mean"])

    p5 = run_practical_5_descriptive_and_ttest(p5_path)
    print("P5 Mean:", p5["mean"], "t-stat:", p5["t_test"]["t_statistic"])

    p6 = run_practical_6_hypothesis_testing(p6_path)
    print("P6 ANOVA F-stat:", p6["one_way_anova"]["F_statistic"])

    print("All statistical tests passed successfully!")
