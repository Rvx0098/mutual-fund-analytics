# Mutual Fund Analytics Platform

## Overview

An end-to-end Mutual Fund Analytics Platform built using Python, SQL, PostgreSQL, and Power BI to analyze fund performance, investor behavior, SIP trends, portfolio allocation, and risk-adjusted returns.

The project processes multiple mutual fund datasets, performs data cleaning and exploratory analysis, calculates advanced financial performance metrics, and delivers interactive business intelligence dashboards for decision-making.

---

## Project Objectives

* Analyze mutual fund performance across multiple schemes.
* Evaluate investor demographics and investment behavior.
* Study SIP growth trends and fund house AUM distribution.
* Calculate risk-adjusted performance metrics.
* Create fund ranking and scorecard models.
* Build interactive Power BI dashboards for business insights.

---

## Tech Stack

### Programming

* Python
* SQL

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

### Database

* PostgreSQL

### Visualization

* Power BI

### Development Environment

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

## Dataset Overview

The project uses 10 mutual fund datasets:

| Dataset                      | Description                    |
| ---------------------------- | ------------------------------ |
| 01_fund_master.csv           | Fund master information        |
| 02_nav_history.csv           | Historical NAV data            |
| 03_aum_by_fund_house.csv     | Assets Under Management        |
| 04_monthly_sip_inflows.csv   | Monthly SIP inflows            |
| 05_category_inflows.csv      | Category-wise inflows          |
| 06_industry_folio_count.csv  | Investor folio counts          |
| 07_scheme_performance.csv    | Fund performance data          |
| 08_investor_transactions.csv | Investor transaction records   |
| 09_portfolio_holdings.csv    | Portfolio holdings and sectors |
| 10_benchmark_indices.csv     | Benchmark index performance    |

---

# Project Structure

```text
mutual_fund_analysis_bluestock/
│
├── Bluestock-Capstone/
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   │
│   ├── charts/
│   ├── reports/
│   └── README.md
│
├── dashboard/
│   ├── mutual_fund_analysis.pbix
│   └── dashboard_requirements.md
│
├── notebooks/
│   ├── Day1_Data_Ingestion.ipynb
│   ├── Day3_EDA.ipynb
│   └── Day4_Performance_Analytics.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   ├── load_to_postgres.py
│   ├── eda_analysis.py
│   ├── kpi_analysis.py
│   ├── performance_analytics.py
│   ├── alpha_beta_analysis.py
│   ├── benchmark_comparison.py
│   └── fund_scorecard.py
│
└── requirements.txt
```

---

# Day 1 — Data Ingestion

### Tasks Completed

* Imported and validated all datasets.
* Performed schema verification.
* Checked missing values.
* Verified record counts.
* Created data quality reports.

### Deliverables

* Data Ingestion Notebook
* Data Quality Summary
* Validation Scripts

---

# Day 2 — Data Cleaning & SQL Database Design

### Tasks Completed

* Cleaned and standardized datasets.
* Created PostgreSQL database schema.
* Loaded cleaned data into PostgreSQL.
* Designed analytical SQL queries.
* Created data dictionary documentation.

### Deliverables

* Cleaned datasets
* PostgreSQL database
* SQL scripts
* Data Dictionary

---

# Day 3 — Exploratory Data Analysis (EDA)

### Analyses Performed

#### NAV Analysis

* NAV trend analysis
* Historical growth visualization

#### AUM Analysis

* Fund house AUM comparison
* Market share analysis

#### SIP Analysis

* Monthly SIP inflow trends
* Growth analysis

#### Investor Analysis

* Age group distribution
* Gender distribution
* Geographic segmentation

#### Portfolio Analysis

* Sector allocation
* Portfolio diversification

### Deliverables

* EDA Notebook
* PNG Visualizations
* EDA Report

---

# Day 4 — Performance Analytics

### Metrics Calculated

#### CAGR

Compound Annual Growth Rate used to evaluate long-term performance.

#### Sharpe Ratio

Measures risk-adjusted return.

#### Sortino Ratio

Measures downside-risk-adjusted return.

#### Alpha

Measures benchmark outperformance.

#### Beta

Measures market sensitivity.

#### Maximum Drawdown

Measures worst peak-to-trough decline.

#### Fund Scorecard

Composite ranking model based on:

* CAGR
* Sharpe Ratio
* Alpha
* Maximum Drawdown

### Deliverables

* Performance Analytics Notebook
* Alpha-Beta Analysis
* Fund Scorecard
* Benchmark Comparison

---

# Power BI Dashboard

The project includes a fully interactive multi-page dashboard.

## Dashboard Pages

### Executive Summary

* Total Funds
* Total Investors
* Total Investment
* Average AUM
* SIP Inflows
* AUM by Fund House

### Investor Analytics

* Gender Distribution
* Age Group Analysis
* Payment Mode Analysis
* City Tier Analysis

### Geographic Analytics

* State-wise Investments
* Investor Distribution
* Average Investment by State

### Portfolio Analytics

* Sector Exposure
* Top Holdings
* Portfolio Allocation Mix
* Sector-wise Portfolio Value

### Fund Performance Analytics

* Top CAGR Funds
* Top Sharpe Ratio Funds
* Top Alpha Funds
* Fund Score Rankings

---

# Key Insights

* Small-cap and mid-cap funds delivered the highest CAGR.
* Mirae Asset Large Cap Fund achieved the highest Sharpe Ratio.
* SBI Small Cap Fund generated the strongest Alpha.
* Banking remained the largest portfolio sector allocation.
* SIP inflows showed consistent growth from 2022–2025.
* Investor participation was highest among the 26–35 age group.

---

# Skills Demonstrated

### Data Analytics

* Data Cleaning
* Exploratory Data Analysis
* KPI Development
* Business Analytics

### Financial Analytics

* Fund Performance Analysis
* Risk Metrics
* Portfolio Analysis
* Benchmark Comparison

### Business Intelligence

* Dashboard Design
* Data Visualization
* KPI Reporting
* Executive Reporting

### Database Management

* PostgreSQL
* SQL Query Development
* Data Modeling

---

# Future Enhancements

* Real-time market data integration
* Automated data pipelines
* Machine Learning-based fund recommendations
* Portfolio optimization models
* Predictive SIP growth forecasting

---

# Author

**Rishit Verma**

Aspiring Data Analyst | Business Analyst | FinTech Analyst

Skills:
Python • SQL • PostgreSQL • Power BI • Data Analytics • Financial Analytics • Machine Learning • Business Intelligence

---

# License

This project is intended for educational, internship, and portfolio purposes.
