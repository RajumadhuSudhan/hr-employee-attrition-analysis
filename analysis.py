"""
HR Employee Attrition Analysis
--------------------------------
Loads the IBM HR Attrition dataset, performs exploratory analysis,
generates visualizations, and exports an Excel summary report.

Usage:
    python analysis.py

Requirements:
    pip install pandas matplotlib seaborn openpyxl
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Configuration ─────────────────────────────────────────────────────────────
DATA_PATH = "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
EXCEL_OUTPUT = "attrition_summary.xlsx"

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 120


# ── 1. Load & Inspect Data ────────────────────────────────────────────────────
def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found at '{path}'.\n"
            "Download it from: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset\n"
            "and place it in the data/ folder."
        )
    df = pd.read_csv(path)
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def basic_info(df):
    print("\n── Basic Info ──────────────────────────────────")
    print(df.dtypes)
    print("\nMissing values:", df.isnull().sum().sum())
    print("\nAttrition value counts:")
    print(df["Attrition"].value_counts())
    attrition_rate = (df["Attrition"] == "Yes").mean() * 100
    print(f"\nOverall Attrition Rate: {attrition_rate:.1f}%")


# ── 2. Helper: Compute Attrition Rate by Group ───────────────────────────────
def attrition_rate_by(df, col):
    """Return a DataFrame with attrition rate (%) per category of col."""
    grouped = df.groupby(col)["Attrition"].apply(
        lambda x: (x == "Yes").sum() / len(x) * 100
    ).reset_index()
    grouped.columns = [col, "Attrition Rate (%)"]
    grouped = grouped.sort_values("Attrition Rate (%)", ascending=False)
    return grouped


# ── 3. Analysis & Visualizations ─────────────────────────────────────────────
def plot_overtime(df):
    data = attrition_rate_by(df, "OverTime")
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(data["OverTime"], data["Attrition Rate (%)"],
                  color=["#e74c3c", "#3498db"], width=0.4)
    ax.bar_label(bars, fmt="%.1f%%", padding=4)
    ax.set_title("Attrition Rate by Overtime Status")
    ax.set_xlabel("Overtime")
    ax.set_ylabel("Attrition Rate (%)")
    ax.set_ylim(0, 50)
    plt.tight_layout()
    plt.savefig("attrition_by_overtime.png")
    plt.close()
    print("Saved: attrition_by_overtime.png")
    return data


def plot_job_role(df):
    data = attrition_rate_by(df, "JobRole")
    fig, ax = plt.subplots(figsize=(9, 5))
    colors = sns.color_palette("coolwarm", len(data))
    bars = ax.barh(data["JobRole"], data["Attrition Rate (%)"], color=colors)
    ax.bar_label(bars, fmt="%.1f%%", padding=4)
    ax.set_title("Attrition Rate by Job Role")
    ax.set_xlabel("Attrition Rate (%)")
    ax.set_xlim(0, 55)
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig("attrition_by_jobrole.png")
    plt.close()
    print("Saved: attrition_by_jobrole.png")
    return data


def plot_income_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    for label, color in [("Yes", "#e74c3c"), ("No", "#3498db")]:
        subset = df[df["Attrition"] == label]["MonthlyIncome"]
        ax.hist(subset, bins=30, alpha=0.6, label=f"Attrition={label}", color=color)
    ax.set_title("Monthly Income Distribution by Attrition")
    ax.set_xlabel("Monthly Income ($)")
    ax.set_ylabel("Employee Count")
    ax.legend()
    plt.tight_layout()
    plt.savefig("attrition_by_income.png")
    plt.close()
    print("Saved: attrition_by_income.png")


def income_summary(df):
    summary = df.groupby("Attrition")["MonthlyIncome"].agg(
        Mean="mean", Median="median", Std="std"
    ).round(2)
    print("\n── Monthly Income by Attrition ─────────────────")
    print(summary)
    return summary


def worklife_summary(df):
    data = attrition_rate_by(df, "WorkLifeBalance")
    data = data.sort_values("WorkLifeBalance")
    print("\n── Attrition by Work-Life Balance Score ────────")
    print(data)
    return data


def tenure_summary(df):
    bins = [0, 2, 5, 10, 100]
    labels = ["0-2 yrs", "3-5 yrs", "6-10 yrs", "10+ yrs"]
    df = df.copy()
    df["TenureBand"] = pd.cut(df["YearsAtCompany"], bins=bins, labels=labels, right=True)
    data = attrition_rate_by(df, "TenureBand")
    print("\n── Attrition by Tenure Band ────────────────────")
    print(data)
    return data


# ── 4. Export Excel Report ────────────────────────────────────────────────────
def export_excel(df, overtime_data, jobrole_data, income_data, worklife_data, tenure_data):
    overall_rate = (df["Attrition"] == "Yes").mean() * 100
    summary_kpis = pd.DataFrame({
        "Metric": [