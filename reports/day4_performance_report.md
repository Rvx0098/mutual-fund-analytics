# Day 4 Report – Performance Analytics & Fund Ranking

## Project Objective

The objective of Day 4 was to perform advanced mutual fund performance analysis using historical NAV data and benchmark index data. The analysis focused on measuring returns, risk, benchmark-relative performance, and developing a quantitative fund ranking framework.

---

# Datasets Used

## 02_nav_history.csv

Contains daily Net Asset Value (NAV) observations for all mutual fund schemes.

### Key Columns

- amfi_code
- date
- nav

---

## 10_benchmark_indices.csv

Contains benchmark index closing values.

### Key Columns

- date
- index_name
- close_value

---

## 07_scheme_performance.csv

Contains scheme-level performance metrics.

### Key Columns

- return_1yr_pct
- return_3yr_pct
- return_5yr_pct
- alpha
- beta
- sharpe_ratio
- sortino_ratio
- max_drawdown_pct

---

# Daily Return Analysis

## Formula

Daily Return = (NAVt − NAVt-1) / NAVt-1

### Purpose

Daily returns provide the foundation for:

- Volatility analysis
- Sharpe Ratio calculation
- Sortino Ratio calculation
- Alpha and Beta estimation

### Outcome

Daily return series were successfully generated for all mutual fund schemes.

---

# CAGR Analysis

## Formula

CAGR = ((Ending NAV / Beginning NAV)^(1 / Years) − 1) × 100

### Top CAGR Funds

| Rank | AMFI Code | CAGR (%) |
|--------|--------|--------:|
| 1 | 120505 | 32.80 |
| 2 | 119598 | 32.40 |
| 3 | 149324 | 32.26 |
| 4 | 148569 | 31.92 |
| 5 | 148567 | 30.95 |

### Insight

Mid-cap and small-cap funds delivered the strongest long-term growth performance.

---

# Sharpe Ratio Analysis

## Formula

Sharpe Ratio = (Return − Risk Free Rate) / Standard Deviation

### Risk-Free Rate Assumption

6.5%

### Purpose

Measures risk-adjusted performance.

### Interpretation

| Sharpe Ratio | Meaning |
|--------------|----------|
| Less than 1 | Poor |
| 1 to 2 | Good |
| Greater than 2 | Excellent |

### Findings

Several equity-oriented schemes achieved Sharpe Ratios above 1.0, indicating favorable risk-adjusted returns.

---

# Sortino Ratio Analysis

## Formula

Sortino Ratio = (Return − Risk Free Rate) / Downside Deviation

### Purpose

Unlike Sharpe Ratio, Sortino Ratio only penalizes downside volatility.

### Findings

Growth-oriented schemes maintained strong Sortino Ratios, indicating efficient downside risk management.

---

# Maximum Drawdown Analysis

## Formula

Drawdown = (Current NAV − Running Peak) / Running Peak

### Purpose

Measures the largest historical decline experienced by an investor.

### Findings

Funds with lower drawdowns demonstrated stronger capital preservation characteristics.

---

# Alpha & Beta Analysis

### Benchmark Used

NIFTY50

### Regression Model

Fund Return = Alpha + Beta × Benchmark Return

---

## Beta

### Formula

Beta = Covariance(Fund, Benchmark) / Variance(Benchmark)

### Interpretation

| Beta | Meaning |
|--------|----------|
| Less than 1 | Less volatile than market |
| Equal to 1 | Similar market volatility |
| Greater than 1 | More volatile than market |

---

## Alpha

### Formula

Alpha = Excess Return Above Benchmark

### Sample Results

| AMFI Code | Alpha | Beta |
|--------|--------:|--------:|
| 119551 | 23.22 | -0.056 |
| 119552 | 19.83 | -0.020 |
| 119598 | 30.11 | 0.074 |

### Findings

Positive Alpha values indicate that the fund outperformed the benchmark after accounting for market risk.

---

# Fund Scorecard Development

## Objective

Develop a composite scoring model to rank mutual funds based on returns, risk, cost, and benchmark performance.

---

## Scoring Framework

| Metric | Weight |
|----------|--------:|
| CAGR | 30% |
| Sharpe Ratio | 25% |
| Alpha | 20% |
| Expense Ratio | 15% |
| Maximum Drawdown | 10% |

---

## Methodology

1. Normalize all metrics using Min-Max Scaling.
2. Reverse-score Expense Ratio.
3. Reverse-score Maximum Drawdown.
4. Apply weighted scoring.
5. Generate a final score between 0 and 100.

---

# Top Ranked Funds

| Rank | Scheme Name | Score |
|--------|-------------|--------:|
| 1 | ICICI Pru Midcap Fund - Regular - Growth | 78.74 |
| 2 | SBI Small Cap Fund - Regular Plan - Growth | 77.40 |
| 3 | DSP Small Cap Fund - Regular - Growth | 76.34 |
| 4 | Mirae Asset Large Cap Fund - Regular - Growth | 75.65 |
| 5 | Kotak Flexicap Fund - Regular - Growth | 74.60 |
| 6 | Mirae Asset Tax Saver Fund - Regular - Growth | 74.17 |
| 7 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 73.06 |
| 8 | Axis Midcap Fund - Regular - Growth | 70.19 |
| 9 | DSP Midcap Fund - Regular - Growth | 69.52 |
| 10 | ICICI Pru Bluechip Fund - Direct - Growth | 68.71 |

---

# Benchmark Comparison

A benchmark comparison visualization was created using:

- Top Ranked Fund
- NIFTY50 Benchmark

### Purpose

The chart enables comparison of:

- Relative performance
- Market outperformance
- Volatility behavior

### Output

benchmark_comparison.png

---

# Generated Outputs

## Processed Data Files

- performance_metrics.csv
- alpha_beta.csv
- fund_scorecard.csv

---

## Visualizations

- benchmark_comparison.png

---

## Scripts

- performance_analytics.py
- alpha_beta_analysis.py
- fund_scorecard.py
- benchmark_comparison.py

---

# Business Recommendations

## 1. Prioritize Risk-Adjusted Returns

Investment decisions should evaluate Sharpe Ratio and Alpha alongside raw returns.

## 2. Monitor Drawdown Risk

Investors with lower risk tolerance should favor funds with smaller maximum drawdowns.

## 3. Utilize Fund Scorecards

Composite scoring systems provide more balanced evaluations than return-only rankings.

## 4. Benchmark Tracking

Regular comparison against NIFTY50 helps assess active management effectiveness.

## 5. Portfolio Diversification

Maintaining exposure across large-cap, mid-cap, and small-cap categories improves long-term risk-adjusted outcomes.

---

# Conclusion

Day 4 successfully implemented advanced mutual fund performance analytics using historical NAV and benchmark data.

### Key Achievements

- Daily Return Calculation
- CAGR Computation
- Sharpe Ratio Analysis
- Sortino Ratio Analysis
- Maximum Drawdown Analysis
- Alpha & Beta Regression
- Fund Scorecard Development
- Benchmark Comparison

These outputs establish the analytical foundation for the final Power BI dashboard and investment intelligence platform.

---

# Project Progress

✅ Day 1 – Data Ingestion & PostgreSQL Setup

✅ Day 2 – Data Cleaning & Database Design

✅ Day 3 – Exploratory Data Analysis

✅ Day 4 – Performance Analytics

🚀 Day 5 – Power BI Dashboard Development