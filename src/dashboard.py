"""
Ticket Prioritization and SLA Dashboard
reads raw support tickets from CSV, applies priority rules based on severity and SLA
"""

import pandas as pd
from datetime import datetime
import os

# Priority mapping rules
SEVERITY_MAP = {
    "Critical": 1,
    "High": 2,
    "Medium": 3,
    "Low": 4
}

SLA_MAP = {
    "1h": 1,
    "4h": 2,
    "1d": 3,
    "3d": 4,
    "7d": 5
}


def load_tickets(filepath: str) -> pd.DataFrame:
    # Load raw tickets from CSV file
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return pd.DataFrame()


def apply_priority_rules(df: pd.DataFrame) -> pd.DataFrame:
    # Assign numerical ranks to severity and SLA, then sort tickets to prioritize the most urgent
    if df.empty:
        return df

    # Map severity and SLA values to numeric ranks
    df["Severity_Rank"] = df["Severity"].map(SEVERITY_MAP).fillna(5)
    df["SLA_Rank"] = df["SLA"].map(SLA_MAP).fillna(6)

    # Priority score = weighted sum (lower is better)
    df["Priority_Score"] = df["Severity_Rank"] * 0.7 + df["SLA_Rank"] * 0.3

    # Sort tickets: lowest score first
    df = df.sort_values(by=["Priority_Score", "Created_At"], ascending=[True, True])
    df = df.reset_index(drop=True)
    df["Priority_Order"] = df.index + 1

    return df


def save_prioritized_data(df: pd.DataFrame, csv_path: str, excel_path: str):
    # Save prioritized results to CSV and Excel dashboard
    if df.empty:
        print("⚠️ No data to save.")
        return

    # Save to CSV
    df.to_csv(csv_path, index=False)

    # Save to Excel (with formatting)
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Prioritized_Tickets")

    print(f"✅ Prioritized CSV saved to {csv_path}")
    print(f"✅ Excel dashboard saved to {excel_path}")


def main():
    # Main workflow for the dashboard pipeline
    # Paths
    raw_path = os.path.join("data", "tickets_raw.csv")
    prioritized_path = os.path.join("data", "tickets_prioritized.csv")
    dashboard_path = os.path.join("output", "dashboard.xlsx")

    # Load tickets
    tickets_df = load_tickets(raw_path)

    if tickets_df.empty:
        return

    # Apply priority rules
    prioritized_df = apply_priority_rules(tickets_df)

    # Save output
    save_prioritized_data(prioritized_df, prioritized_path, dashboard_path)


if __name__ == "__main__":
    main()