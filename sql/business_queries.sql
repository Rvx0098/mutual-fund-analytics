-- Top 10 Funds by AUM

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;


-- Best 5-Year Performers

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- Fund House Market Share

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM scheme_performance
GROUP BY fund_house
ORDER BY total_aum DESC;

SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS avg_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY avg_nav DESC
LIMIT 10;

SELECT
    state,
    ROUND(SUM(amount_inr),2) AS total_investment
FROM investor_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;

SELECT
    scheme_name,
    expense_ratio_pct
FROM fund_master
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

SELECT
    payment_mode,
    COUNT(*) AS transaction_count
FROM investor_transactions
GROUP BY payment_mode
ORDER BY transaction_count DESC;

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

SELECT
    sector,
    ROUND(SUM(weight_pct),2) AS total_weight
FROM portfolio_holdings
GROUP BY sector
ORDER BY total_weight DESC;

SELECT
    category,
    ROUND(SUM(net_inflow_crore),2) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;