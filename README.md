# Waze User Churn EDA 


**Tech:** Python, pandas, numpy  
**Project type:** Exploratory Data Analysis + simple feature engineering  
**Goal:** Compare behavior patterns between churned vs retained users.

## Why this repo stands out
- Uses **clean, beginner-level Python** (no heavy ML libraries)
- Produces **shareable outputs** (`reports/results.md`, `reports/eda_summary.csv`)
- Dataset is **not uploaded** (license restrictions), but the repo still runs using a **synthetic sample dataset**

## What I analyzed
- Basic data checks (rows/columns, missing values)
- Churn vs retained split (label balance)
- Simple feature engineering:
  - km_per_drive = driven_km_drives / drives
  - km_per_driving_day = driven_km_drives / driving_days
  - minutes_per_drive = duration_minutes_drives / drives
- Median comparison by label
- Device split by label

## Data disclaimer
This repository does not include the original dataset used in the course/lab environment because it is not publicly redistributable.
To run with the real dataset, place it locally at: `data/waze.csv`.

## Quickstart (runs in under a minute)
```bash
pip install -r requirements.txt
python main.py







