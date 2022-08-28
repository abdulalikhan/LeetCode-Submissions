# Write your MySQL query statement below
SELECT STOCK_NAME, SUM(
                    CASE
                        WHEN OPERATION = 'Buy'
                            THEN -PRICE
                            ELSE PRICE
                    END) as CAPITAL_GAIN_LOSS
FROM STOCKS
GROUP BY STOCK_NAME;