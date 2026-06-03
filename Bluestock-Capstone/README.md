# Mutual Fund Analytics Capstone Project

## Overview

This project is an end-to-end Mutual Fund Analytics solution built using Python, PostgreSQL, SQL, and Data Analytics techniques. The objective is to analyze mutual fund performance, investor behavior, SIP growth trends, portfolio composition, and industry-level investment patterns to generate actionable business insights.

---

## Project Objectives

* Analyze mutual fund scheme performance.
* Study SIP (Systematic Investment Plan) growth trends.
* Understand investor demographics and behavior.
* Explore geographic investment patterns.
* Evaluate portfolio sector exposure.
* Generate business insights for asset management companies.
* Build a foundation for dashboard development and reporting.

---

## Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

### Database

* PostgreSQL
* SQLAlchemy
* psycopg2

### Development Tools

* VS Code
* Jupyter Notebook
* pgAdmin
* Git
* GitHub

---

## Project Structure

```text
mutual_fund_analysis_bluestock
│
├── Bluestock-Capstone
│   ├── charts
│   ├── dashboard
│   ├── data
│   │   ├── raw
│   │   ├── processed
│   │   └── live_nav
│   │
│   ├── notebooks
│   └── reports
│
├── scripts
├── sql
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Datasets Used

| Dataset               | Description                |
| --------------------- | -------------------------- |
| Fund Master           | Mutual fund metadata       |
| NAV History           | Historical NAV values      |
| AUM by Fund House     | Assets under management    |
| Monthly SIP Inflows   | SIP growth trends          |
| Category Inflows      | Category-wise inflows      |
| Industry Folio Count  | Investor folio statistics  |
| Scheme Performance    | Fund return metrics        |
| Investor Transactions | Investor activity data     |
| Portfolio Holdings    | Fund portfolio composition |
| Benchmark Indices     | Market benchmark data      |

---

## Day 1 – Data Engineering & Ingestion

### Activities Completed

* Project structure creation
* Dependency installation
* Dataset profiling and validation
* AMFI code verification
* PostgreSQL database setup
* Schema design and table creation
* ETL pipeline development
* Data loading into PostgreSQL
* Data quality validation

### Deliverables

* data_ingestion.py
* live_nav_fetch.py
* amfi_validation.py
* load_to_postgres.py
* day1_data_quality_summary.md

---

## Day 2 – Exploratory Data Analysis

### Analysis Performed

#### Fund Analysis

* Top Mutual Funds by AUM
* Scheme Performance Analysis

#### SIP Analysis

* Monthly SIP Growth Trends

#### Investor Analysis

* Age Distribution
* Gender Distribution
* City Tier Distribution
* Payment Mode Analysis

#### Geographic Analysis

* Top States by Investment Amount

#### Portfolio Analysis

* Sector Exposure Analysis

---

## Key Insights

### SIP Growth

Monthly SIP inflows increased from approximately ₹11,500 Crore to over ₹31,000 Crore, indicating strong growth in retail investor participation.

### Geographic Concentration

Top contributing states include:

* Tamil Nadu
* Punjab
* Madhya Pradesh
* Rajasthan
* Gujarat

These states represent significant opportunities for investor acquisition and market expansion.

### Portfolio Sector Exposure

Top portfolio sectors:

1. Banking
2. Information Technology (IT)
3. Pharma
4. Automobile
5. Utilities

This indicates strong exposure to sectors critical to India's economic growth.

### Investor Trends

* Growing retail participation
* Strong adoption of digital payment methods
* Significant contribution from Tier-1 and Tier-2 cities

---

## Visualizations Generated

* Top Funds by AUM
* SIP Growth Trend
* Investor Age Distribution
* Gender Distribution
* City Tier Distribution
* Payment Mode Distribution
* State-wise Investments
* Portfolio Sector Exposure

---

## Database Design

The PostgreSQL database contains:

* fund_master
* nav_history
* aum_by_fund_house
* monthly_sip_inflows
* category_inflows
* industry_folio_count
* scheme_performance
* investor_transactions
* portfolio_holdings
* benchmark_indices

---

## Business Value

This project demonstrates:

* Data Engineering
* SQL Analysis
* Exploratory Data Analysis
* Business Intelligence
* Financial Data Analytics
* Data Visualization
* Database Design
* ETL Development

---

## Future Enhancements

### Day 3

* KPI Dashboard Development
* Advanced SQL Analytics
* Dashboard Metrics

### Day 4

* Power BI Dashboard
* Interactive Visualizations

### Day 5

* Final Reporting
* Presentation Preparation
* Project Documentation

---

## Author

**Rishit Verma**

Aspiring Data Analyst | Business Analyst | FinTech Analyst

GitHub: https://github.com/Rvx0098
