-- DIMENSION TABLES

CREATE TABLE dim_fund (
    amfi_code BIGINT PRIMARY KEY,
    scheme_name VARCHAR(255),
    fund_house VARCHAR(255),
    category VARCHAR(100),
    sub_category VARCHAR(100),
    expense_ratio_pct NUMERIC(5,2),
    risk_category VARCHAR(50)
);

CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY
);

-- FACT TABLES

CREATE TABLE fact_nav (
    amfi_code BIGINT,
    nav_date DATE,
    nav NUMERIC(12,4),
    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    investor_id VARCHAR(50),
    transaction_date DATE,
    amfi_code BIGINT,
    transaction_type VARCHAR(50),
    amount_inr NUMERIC(15,2)
);

CREATE TABLE fact_performance (
    amfi_code BIGINT,
    return_1yr_pct NUMERIC(10,2),
    return_3yr_pct NUMERIC(10,2),
    return_5yr_pct NUMERIC(10,2),
    alpha NUMERIC(10,4),
    beta NUMERIC(10,4),
    sharpe_ratio NUMERIC(10,4)
);

CREATE TABLE fact_aum (
    report_date DATE,
    fund_house VARCHAR(255),
    aum_crore NUMERIC(15,2)
);