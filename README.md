# Ticket Prioritization and SLA Dashboard

This project automates the **prioritization of support tickets** based on severity and SLA (Service Level Agreement).  
It produces both a **CSV output** and an **Excel dashboard** that highlights the most urgent tickets for IT/Application Support teams.

---

## Features
- Reads raw ticket data from CSV
- Applies priority rules:
  - Critical issues ranked highest
  - SLA deadlines factored in
- Generates sorted output with `Priority_Order`
- Outputs:
  - `tickets_prioritized.csv`
  - `dashboard.xlsx`

---

## Project Structure
Ticket-Prioritization-and-Service-Level-Agreement-(SLA)-Dashboard/
├─ src/
│   └─ dashboard.py      # processes tickets
├─ data/
│   ├─ tickets_raw.csv   # input (messy)
│   └─ tickets_prioritized.csv # output (clean)
├─ output/
│   └─ dashboard.xlsx    # Excel dashboard
├─ README.md
└─ benchmark.md

---

## Project Instructions

**Install dependencies, Run, Check Results**
  ```bash
  pip install pandas openpyxl

  python src/dashboard.py

