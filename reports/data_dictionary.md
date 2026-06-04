# Data Dictionary

## 01_fund_master.csv

| Column            | Type    | Description                   |
| ----------------- | ------- | ----------------------------- |
| amfi_code         | Integer | Unique AMFI scheme identifier |
| fund_house        | Text    | Asset management company      |
| scheme_name       | Text    | Mutual fund scheme name       |
| category          | Text    | Fund category                 |
| sub_category      | Text    | Fund sub-category             |
| expense_ratio_pct | Decimal | Expense ratio percentage      |
| risk_category     | Text    | Risk classification           |

---

## 02_nav_history.csv

| Column    | Type    | Description          |
| --------- | ------- | -------------------- |
| amfi_code | Integer | Scheme identifier    |
| date      | Date    | NAV observation date |
| nav       | Decimal | Net Asset Value      |

---

## 03_aum_by_fund_house.csv

| Column     | Type    | Description             |
| ---------- | ------- | ----------------------- |
| date       | Date    | Reporting date          |
| fund_house | Text    | Fund house              |
| aum_crore  | Decimal | Assets under management |

---

## 04_monthly_sip_inflows.csv

| Column           | Type    | Description           |
| ---------------- | ------- | --------------------- |
| month            | Text    | Month                 |
| sip_inflow_crore | Decimal | Monthly SIP inflow    |
| yoy_growth_pct   | Decimal | Year-over-year growth |

---

## 05_category_inflows.csv

| Column           | Type    | Description       |
| ---------------- | ------- | ----------------- |
| month            | Text    | Month             |
| category         | Text    | Fund category     |
| net_inflow_crore | Decimal | Net inflow amount |

---

## 06_industry_folio_count.csv

| Column             | Type    | Description       |
| ------------------ | ------- | ----------------- |
| month              | Text    | Month             |
| total_folios_crore | Decimal | Total folio count |

---

## 07_scheme_performance.csv

| Column         | Type    | Description       |
| -------------- | ------- | ----------------- |
| return_1yr_pct | Decimal | One-year return   |
| return_3yr_pct | Decimal | Three-year return |
| return_5yr_pct | Decimal | Five-year return  |
| alpha          | Decimal | Alpha metric      |
| beta           | Decimal | Beta metric       |
| sharpe_ratio   | Decimal | Sharpe ratio      |

---

## 08_investor_transactions.csv

| Column           | Type    | Description             |
| ---------------- | ------- | ----------------------- |
| investor_id      | Text    | Investor identifier     |
| transaction_type | Text    | SIP/Lumpsum/Redemption  |
| amount_inr       | Decimal | Transaction amount      |
| kyc_status       | Text    | KYC verification status |

---

## 09_portfolio_holdings.csv

| Column       | Type    | Description           |
| ------------ | ------- | --------------------- |
| stock_symbol | Text    | Stock ticker          |
| sector       | Text    | Sector classification |
| weight_pct   | Decimal | Portfolio weight      |

---

## 10_benchmark_indices.csv

| Column      | Type    | Description     |
| ----------- | ------- | --------------- |
| date        | Date    | Index date      |
| index_name  | Text    | Benchmark index |
| close_value | Decimal | Closing value   |
