## Data Engineering Zoomcamp Homework 4
# Q3
SELECT COUNT(*) AS record_count \
FROM {{ ref('fct_monthly_zone_revenue') }}; \
# Q4
SELECT \
    pickup_zone,\
    SUM(revenue_monthly_total_amount) AS total_revenue\
FROM {{ ref('fct_monthly_zone_revenue') }}\
WHERE service_type = 'Green'\
  AND year = 2020\
GROUP BY pickup_zone\
ORDER BY total_revenue DESC\
LIMIT 1; \
# Q5
SELECT \
    SUM(total_monthly_trips) AS total_trips \
FROM {{ ref('fct_monthly_zone_revenue') }} \
WHERE service_type = 'Green' \
  AND year = 2019 \
  AND month = 10; \