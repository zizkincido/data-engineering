## Homework 2: Workflow Orchestration

# Q1
On gcp you can see every csv file size with bucket list.
# Q2
Before render it was {{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv but after we gave inputs it became green_tripdata_2020-04.csv 
# Q3
SELECT COUNT(*) AS row_count \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata` \
WHERE tpep_pickup_datetime >= '2020-01-01' \
  AND tpep_pickup_datetime < '2021-01-01' \

# Q4
SELECT COUNT(*) AS row_count \
FROM `dt-eng-zmcmp.zoomcamp.green_tripdata` \
WHERE lpep_pickup_datetime >= '2020-01-01' \
  AND lpep_pickup_datetime < '2021-01-01'; \

# Q5
SELECT COUNT(*) AS row_count
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata` \
WHERE tpep_pickup_datetime >= '2021-03-01' \
  AND tpep_pickup_datetime < '2021-04-01'; \

# Q6 
America/New_York
