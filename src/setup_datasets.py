import os
import shutil
import requests
import pandas as pd
from sklearn.datasets import load_breast_cancer

def main():
    project_dir = r"C:\Users\HP\.gemini\antigravity-ide\scratch\food-delivery-time-prediction"
    raw_dir = os.path.join(project_dir, "data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    downloads = r"C:\Users\HP\Downloads"

    # 1. Download Food Delivery Dataset
    food_url = "https://raw.githubusercontent.com/SaloniJhalani/Food-Delivery-Time-Prediction-Model/main/data/train.csv"
    food_dest = os.path.join(raw_dir, "food_delivery_train.csv")
    if not os.path.exists(food_dest):
        print("Downloading Food Delivery dataset...")
        r = requests.get(food_url, timeout=30)
        with open(food_dest, "wb") as f:
            f.write(r.content)
        print("Saved food_delivery_train.csv, size:", os.path.getsize(food_dest))
    else:
        print("food_delivery_train.csv already exists.")

    # 2. Download Medical Insurance Dataset
    ins_url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
    ins_dest = os.path.join(raw_dir, "medical_insurance.csv")
    if not os.path.exists(ins_dest):
        print("Downloading Medical Insurance dataset...")
        r = requests.get(ins_url, timeout=30)
        with open(ins_dest, "wb") as f:
            f.write(r.content)
        print("Saved medical_insurance.csv, size:", os.path.getsize(ins_dest))
    else:
        print("medical_insurance.csv already exists.")

    # 3. Create breast cancer dataset
    bc_dest = os.path.join(raw_dir, "breast_cancer_data.csv")
    if not os.path.exists(bc_dest):
        bc = load_breast_cancer(as_frame=True)
        df_bc = bc.frame
        df_bc["diagnosis"] = df_bc["target"].map({0: "M", 1: "B"})
        df_bc.to_csv(bc_dest, index=False)
        print("Saved breast_cancer_data.csv, shape:", df_bc.shape)

    # 4. Copy existing practical datasets from Downloads
    copy_list = [
        "student_training_performance_500.csv",
        "SOCR-HeightWeight.csv",
        "StudentPerformanceFactors.csv",
        "Housing.csv",
        "train.csv",
        "hour.csv"
    ]
    for cf in copy_list:
        src = os.path.join(downloads, cf)
        dst = os.path.join(raw_dir, cf)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
            print(f"Copied {cf} to data/raw")
        elif os.path.exists(dst):
            print(f"{cf} already present in data/raw")

    print("\nDataset setup complete!")

if __name__ == "__main__":
    main()
