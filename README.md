# HR Employee Attrition Analysis

A beginner-to-intermediate data analysis project exploring patterns behind employee attrition using SQL, Python, and Excel. Built as a portfolio project to demonstrate end-to-end data analysis skills.

## Project Overview

Employee attrition is costly. This project analyzes the [IBM HR Analytics Employee Attrition dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) to uncover which factors — such as job role, overtime, salary, and work-life balance — are most strongly associated with employees leaving a company.

## Skills Demonstrated

- **SQL**: Data exploration and aggregation queries
- **Python**: Data cleaning, analysis, and visualization (pandas, matplotlib, seaborn)
- **Excel**: Summary report with key findings (generated via Python)

## Project Structure

```
hr-attrition-analysis/
├── README.md
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv   ← download from Kaggle
├── queries.sql          ← SQL exploration queries
├── analysis.py          ← Python analysis + visualizations + Excel export
```

## Setup & Usage

### 1. Get the Data

Download the dataset from Kaggle:
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

Place the CSV file at:
```
data/WA_Fn-UseC_-HR-Employee-Attrition.csv
```

### 2. Install Dependencies

```bash
pip install pandas matplotlib seaborn openpyxl
```

### 3. Run the SQL Queries

The `queries.sql` file contains standalone SQL queries written in standard SQL. You can run them using:
- **SQLite** (via DB Browser for SQLite — free and easy)
- **DuckDB** (run directly on CSV)
- Any other SQL environment

To use with DuckDB in Python:
```python
import duckdb
duckdb.query("SELECT * FROM 'data/WA_Fn-UseC_-HR-Employee-Attrition.csv' LIMIT 5").df()
```

### 4. Run the Python Analysis

```bash
python analysis.py
```

This will:
- Load and clean the dataset
- Print attrition statistics to the console
- Generate and save visualizations as PNG files
- Export an Excel summary report: `attrition_summary.xlsx`

## Key Findings

| Factor | Finding |
|---|---|
| Overtime | Employees working overtime attrit at ~30% vs ~10% without |
| Job Role | Sales Representatives have the highest attrition rate (~40%) |
| Monthly Income | Employees who left earned ~$1,500 less on average |
| Work-Life Balance | Lower scores strongly correlate with higher attrition |
| Years at Company | Highest attrition risk in the first 1–3 years |

## Output Files

After running `analysis.py`:
- `attrition_by_overtime.png`
- `attrition_by_jobrole.png`
- `attrition_by_income.png`
- `attrition_summary.xlsx`

## Dataset Credit

IBM HR Analytics Employee Attrition & Performance — fictional dataset created by IBM data scientists, available on Kaggle.