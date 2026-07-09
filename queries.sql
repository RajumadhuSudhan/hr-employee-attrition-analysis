-- HR Employee Attrition Analysis
-- SQL Exploration Queries
-- Compatible with SQLite, DuckDB, PostgreSQL, MySQL (minor syntax differences may apply)
-- If using DuckDB on the raw CSV, replace 'employees' with 'data/WA_Fn-UseC_-HR-Employee-Attrition.csv'

-- ============================================================
-- 1. Overall attrition rate
-- ============================================================
SELECT
    Attrition,
    COUNT(*) AS employee_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM employees
GROUP BY Attrition;


-- ============================================================
-- 2. Attrition rate by Department
-- ============================================================
SELECT
    Department,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS left_count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY Department
ORDER BY attrition_rate_pct DESC;


-- ============================================================
-- 3. Attrition rate by Job Role
-- ============================================================
SELECT
    JobRole,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS left_count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY JobRole
ORDER BY attrition_rate_pct DESC;


-- ============================================================
-- 4. Attrition rate by Overtime status
-- ============================================================
SELECT
    OverTime,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS left_count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY OverTime
ORDER BY attrition_rate_pct DESC;


-- ============================================================
-- 5. Average Monthly Income by Attrition status
-- ============================================================
SELECT
    Attrition,
    ROUND(AVG(MonthlyIncome), 2) AS avg_monthly_income,
    ROUND(MIN(MonthlyIncome), 2) AS min_income,
    ROUND(MAX(MonthlyIncome), 2) AS max_income
FROM employees
GROUP BY Attrition;


-- ============================================================
-- 6. Attrition by Work-Life Balance score (1=Bad, 4=Best)
-- ============================================================
SELECT
    WorkLifeBalance,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS left_count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY WorkLifeBalance
ORDER BY WorkLifeBalance;


-- ============================================================
-- 7. Attrition by Years at Company (binned)
-- ============================================================
SELECT
    CASE
        WHEN YearsAtCompany <= 2  THEN '0-2 years'
        WHEN YearsAtCompany <= 5  THEN '3-5 years'
        WHEN YearsAtCompany <= 10 THEN '6-10 years'
        ELSE '10+ years'
    END AS tenure_band,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS left_count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY tenure_band
ORDER BY MIN(YearsAtCompany);


-- ============================================================
-- 8. Age distribution of employees who left vs stayed
-- ============================================================
SELECT
    Attrition,
    ROUND(AVG(Age), 1) AS avg_age,
    MIN(Age) AS min_age,
    MAX(Age) AS max_age
FROM employees
GROUP BY Attrition;


-- ============================================================
-- 9. Top factors combined: Overtime + Job Satisfaction
-- ============================================================
SELECT
    OverTime,
    JobSatisfaction,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS left_count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS attrition_rate_pct
FROM employees
GROUP BY OverTime, JobSatisfaction
ORDER BY attrition_rate_pct DESC;