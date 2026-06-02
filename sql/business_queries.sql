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