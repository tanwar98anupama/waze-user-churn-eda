import pandas as pd
import numpy as np
import os

DATA_PATH = "data/waze.csv"
SAMPLE_PATH = "data/sample_dataset.csv"
OUT_SUMMARY = "reports/eda_summary.csv"
OUT_RESULTS = "reports/results.md"


def safe_divide(a: pd.Series, b: pd.Series) -> pd.Series:
    """Avoid divide-by-zero by converting 0 to NaN."""
    b = b.replace(0, np.nan)
    return a / b


def main():
    # 1) Load data
    path = DATA_PATH if os.path.exists(DATA_PATH) else SAMPLE_PATH
    df = pd.read_csv(path)

    # 2) Basic info
    rows, cols = df.shape

    # 3) Missingness (top 10)
    missing_pct = (df.isna().mean() * 100).round(2).sort_values(ascending=False)

    # 4) Feature engineering using column names
    df["km_per_drive"] = safe_divide(df["driven_km_drives"], df["drives"])
    df["km_per_driving_day"] = safe_divide(df["driven_km_drives"], df["driving_days"])
    df["minutes_per_drive"] = safe_divide(df["duration_minutes_drives"], df["drives"])
    df["sessions_per_day"] = safe_divide(df["total_sessions"], df["n_days_after_onboarding"])

    # 5) Label balance
    label_counts = df["label"].value_counts(dropna=False)
    label_pct = (label_counts / label_counts.sum() * 100).round(2)
    label_summary = pd.DataFrame({"count": label_counts, "pct": label_pct})

    # 6) Median comparison by label (beginner-friendly and useful)
    metric_cols = [
        "drives",
        "driving_days",
        "total_sessions",
        "n_days_after_onboarding",
        "driven_km_drives",
        "duration_minutes_drives",
        "km_per_drive",
        "km_per_driving_day",
        "minutes_per_drive",
        "sessions_per_day",
    ]
    median_by_label = df.groupby("label")[metric_cols].median(numeric_only=True).round(2)

    # 7) Device split by label (% within each label)
    device_pct = (pd.crosstab(df["device"], df["label"], normalize="columns") * 100).round(2)

    os.makedirs("reports", exist_ok=True)

    # 8) Write one CSV output with sections (easy to review)
    with open(OUT_SUMMARY, "w", encoding="utf-8") as f:
        f.write("SECTION: BASIC_INFO\n")
        f.write(f"rows,{rows}\n")
        f.write(f"columns,{cols}\n\n")

        f.write("SECTION: MISSINGNESS_TOP_10 (percent)\n")
        missing_pct.head(10).to_csv(f, header=["missing_pct"])
        f.write("\n")

        f.write("SECTION: LABEL_BALANCE\n")
        label_summary.to_csv(f)
        f.write("\n")

        f.write("SECTION: MEDIAN_BY_LABEL\n")
        median_by_label.to_csv(f)
        f.write("\n")

        f.write("SECTION: DEVICE_SPLIT_PCT\n")
        device_pct.to_csv(f)
        f.write("\n")

    # 9) Write a short Markdown results file 
    with open(OUT_RESULTS, "w", encoding="utf-8") as f:
        f.write("# Results Summary (Auto-generated)\n\n")
        f.write(f"- Dataset size: **{rows} rows × {cols} columns**\n")
        f.write(f"- Highest missing column: **{missing_pct.index[0]} = {missing_pct.iloc[0]}%**\n\n")

        f.write("## Label Balance\n\n")
        f.write(label_summary.to_markdown())
        f.write("\n\n")

        f.write("## Median Metrics by Label\n\n")
        f.write(median_by_label.to_markdown())
        f.write("\n\n")

        f.write("## Device Split (% within each label)\n\n")
        f.write(device_pct.to_markdown())
        f.write("\n\n")

        f.write("## Notes\n")
        f.write("- This project intentionally focuses on EDA + simple feature engineering using pandas/numpy.\n")
        f.write("- Next step would be a churn model, but not included to keep this beginner-realistic.\n")

    print("Done. Created:")
    print("-", OUT_SUMMARY)
    print("-", OUT_RESULTS)


if __name__ == "__main__":
    main()
