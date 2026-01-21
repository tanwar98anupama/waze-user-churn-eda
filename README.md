# Waze User Churn EDA 

**Tools:** Python, pandas, numpy  
**Live page:** ( link )

## What this project does
A simple exploratory data analysis (EDA) project to compare **churn vs retained** Waze users using Python.

## Dataset columns
ID, label, sessions, drives, total_sessions, n_days_after_onboarding, total_navigations_fav1, total_navigations_fav2,
driven_km_drives, duration_minutes_drives, activity_days, driving_days, device

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
This repository does not include the raw dataset used for analysis. The data was provided as part of a course/lab environment and is not publicly redistributable. To reproduce the results, place your local copy of the dataset at data/waze.csv and run:
pip install -r requirements.txt
python main.py






