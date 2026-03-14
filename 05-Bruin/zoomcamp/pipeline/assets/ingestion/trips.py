"""@bruin
name: ingestion.trips

type: python
image: python:3.11
connection: duckdb-default
materialization:
  type: table
  strategy: append
columns:
  - name: taxi_type
    type: text
  - name: pickup_datetime
    type: timestamp
  - name: dropoff_datetime
    type: timestamp
  - name: passenger_count
    type: integer
  - name: trip_distance
    type: float
  - name: extracted_at
    type: timestamp
@bruin"""

import os
import json
from datetime import datetime

import pandas as pd
import requests


def _parse_vars():
    vars_json = os.getenv("BRUIN_VARS", "{}")
    return json.loads(vars_json)


def materialize():
    """
    Fetch raw taxi trip CSVs for the run window and return a
    pandas.DataFrame that Bruin will load into the destination.

    The asset relies on the built‑in environment variables
    `BRUIN_START_DATE` / `BRUIN_END_DATE` and a pipeline variable
    `taxi_types` (a list such as ["yellow","green"]).
    """
    start = os.getenv("BRUIN_START_DATE")
    end = os.getenv("BRUIN_END_DATE")
    if not start or not end:
        raise RuntimeError("BRUIN_START_DATE/BRUIN_END_DATE must be set")

    taxi_vars = _parse_vars()
    taxi_types = taxi_vars.get("taxi_types", ["yellow"])

    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)

    data_frames = []
    current = start_dt.replace(day=1)
    while current <= end_dt:
        yyyy_mm = current.strftime("%Y-%m")
        for taxi in taxi_types:
            url = (
                f"https://s3.amazonaws.com/nyc-tlc/trip+data/"
                f"{taxi}_tripdata_{yyyy_mm}.csv"
            )
            try:
                df = pd.read_csv(url)
            except Exception:
                # missing file or network error; skip quietly
                continue
            df["taxi_type"] = taxi
            df["extracted_at"] = datetime.utcnow()
            data_frames.append(df)
        # advance one month
        if current.month == 12:
            current = current.replace(year=current.year + 1, month=1)
        else:
            current = current.replace(month=current.month + 1)

    if not data_frames:
        # return an empty schema-aligned frame
        return pd.DataFrame(
            columns=[
                "taxi_type",
                "pickup_datetime",
                "dropoff_datetime",
                "passenger_count",
                "trip_distance",
                "extracted_at",
            ]
        )

    result = pd.concat(data_frames, ignore_index=True)
    # keep only the columns we care about
    return result[
        [
            "taxi_type",
            "pickup_datetime",
            "dropoff_datetime",
            "passenger_count",
            "trip_distance",
            "extracted_at",
        ]
    ]
