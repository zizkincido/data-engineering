## Data Engineering Zoomcamp Homework 3
Create external table from gcs bucket \
CREATE OR REPLACE EXTERNAL TABLE `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024_ext` \
OPTIONS ( \
  format = 'PARQUET', \
  uris = ['gs://dt-eng-zmpcmp-bucket/yellow_tripdata_2024-*.parquet'] \
); \
Create materialized table from external table \
CREATE OR REPLACE TABLE `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024` \
AS \
SELECT * \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024_ext`; \
# Q1
SELECT COUNT(*) AS row_count \ 
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024` \
# Q2
SELECT \
  COUNT(DISTINCT PULocationID) AS distinct_pu_locations \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024_ext`; \
SELECT \
  COUNT(DISTINCT PULocationID) AS distinct_pu_locations \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024`; \
# Q3
SELECT PULocationID \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024`; \
SELECT \
  PULocationID, \
  DOLocationID \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024`; \
# Q4
SELECT COUNT(*) AS zero_fare_count \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024` \
WHERE fare_amount = 0; \
# Q5
CREATE OR REPLACE TABLE `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024_optimized`\
PARTITION BY DATE(tpep_dropoff_datetime) \
CLUSTER BY VendorID \
AS \
SELECT * \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024`; \
# Q6
SELECT DISTINCT VendorID \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024` \
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15'; \
SELECT DISTINCT VendorID \
FROM `dt-eng-zmcmp.zoomcamp.yellow_tripdata_2024_optimized` \
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15'; \

