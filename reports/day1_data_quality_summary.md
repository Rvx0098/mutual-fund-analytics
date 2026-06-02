# Day 1 Summary – Data Ingestion & Database Setup

## Project: Mutual Fund Analytics Capstone

### Objectives Completed

The primary goal of Day 1 was to establish the data foundation for the Mutual Fund Analytics project by organizing project resources, validating datasets, setting up the database environment, and building an automated data ingestion pipeline.

---

## 1. Project Setup

Created a structured project directory to support data engineering, analytics, reporting, and dashboard development.

### Folder Structure

* data/raw
* data/processed
* data/raw/live_nav
* scripts
* sql
* reports
* dashboard
* notebooks
* charts

### Environment Setup

Installed and configured:

* Python 3.13
* Virtual Environment (venv)
* PostgreSQL
* pgAdmin

### Libraries Installed

* pandas
* numpy
* matplotlib
* seaborn
* plotly
* sqlalchemy
* psycopg2-binary
* requests
* scipy
* jupyter

Generated and maintained a requirements.txt file for reproducibility.

---

## 2. Dataset Ingestion & Profiling

Successfully loaded and reviewed all 10 provided datasets using Pandas.

### Datasets Analyzed

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

### Profiling Performed

For each dataset:

* Shape analysis
* Data type inspection
* First five records review
* Missing value identification
* Duplicate record checks

### Key Dataset Sizes

| Dataset               |   Rows |
| --------------------- | -----: |
| Fund Master           |     40 |
| NAV History           | 46,000 |
| AUM by Fund House     |     90 |
| Monthly SIP Inflows   |     48 |
| Category Inflows      |    144 |
| Industry Folio Count  |     21 |
| Scheme Performance    |     40 |
| Investor Transactions | 32,778 |
| Portfolio Holdings    |    322 |
| Benchmark Indices     |  8,050 |

Total records processed: ~87,500+

---

## 3. Fund Master Exploration

Analyzed the master reference dataset to understand:

* Fund houses
* Categories
* Sub-categories
* Risk classifications
* AMFI scheme codes

Validated the overall structure and consistency of fund metadata.

---

## 4. AMFI Code Validation

Performed integrity validation between:

* Fund Master
* NAV History

### Validation Result

* All AMFI codes from Fund Master were present in NAV History.
* No missing scheme mappings detected.

Result: Validation Passed

---

## 5. PostgreSQL Database Design

Created database:

bluestock_mf

Designed and implemented 10 relational tables:

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

## 6. ETL Pipeline Development

Developed automated data loading scripts using:

* Pandas
* SQLAlchemy
* PostgreSQL

### Activities Completed

* CSV ingestion
* Schema mapping
* Column renaming and transformations
* Database insertion
* Validation checks

### Data Successfully Loaded

* Fund Master
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Count
* Scheme Performance
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

---

## 7. Live NAV Integration

Developed a script to fetch real-time NAV data from:

https://api.mfapi.in

Target schemes included:

* HDFC Top 100 Direct
* SBI Bluechip
* ICICI Bluechip
* Nippon Large Cap
* Axis Bluechip
* Kotak Bluechip

### Outcome

The API endpoint returned HTTP 502 Bad Gateway during testing.

The integration script was successfully implemented, but execution was blocked due to temporary upstream service unavailability.

---

## 8. Challenges Resolved

### Technical Issues Solved

* Python installation conflicts
* Virtual environment setup failures
* PostgreSQL connectivity issues
* Schema-column mismatches
* ETL pipeline debugging
* Table creation inconsistencies
* Data loading validation

---

## Deliverables Produced

### Scripts

* data_ingestion.py
* live_nav_fetch.py
* fund_master_analysis.py
* amfi_validation.py
* load_to_postgres.py

### Database

* PostgreSQL database configured
* 10 analytical tables populated

### Documentation

* requirements.txt
* Day 1 summary
* Data quality observations

---

## Conclusion

Day 1 successfully established the complete data engineering foundation for the Mutual Fund Analytics Capstone Project. All datasets were validated, loaded into PostgreSQL, and prepared for downstream analytics. The project is now ready for Exploratory Data Analysis (EDA), KPI generation, business insights, and dashboard development in Day 2.
