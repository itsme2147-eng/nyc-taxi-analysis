# Real-World Dataset Analysis Project: NYC Taxi Trips, March 2019

Task 3 of the AI/ML Research Specialist virtual internship (Yuva Intern, Thiruvananthapuram).
End-to-end analysis of real taxi trip records: selection, exploration, cleaning, EDA, visualisation and interpretation.

## Dataset
NYC yellow and green taxi trips, March 2019 (6,433 trips), based on the NYC Taxi & Limousine Commission
Trip Record Data (https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). This copy is the sample
distributed in the seaborn-data repository. URL and SHA-256 checksum are in `data/SOURCE.md`.

## Objective -> where covered
| # | Objective | Location |
|---|-----------|----------|
| 1 | Select a real-world dataset and its context | notebook Part 1, `data/SOURCE.md` |
| 2 | Explore the dataset | notebook Part 2 |
| 3 | Clean and preprocess | notebook Part 3, `outputs/cleaning_log.csv` |
| 4 | Exploratory data analysis | notebook Part 4 |
| 5 | Visualisations (14 figures) | notebook Part 5, `outputs/figures/` |
| 6 | Insights and interpretations | notebook Part 6, `docs/Task3_NYC_Taxi_Analysis_Report.docx` |

## Run it
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/download_data.py                             # downloads raw data + writes data/SOURCE.md
jupyter notebook notebooks/NYC_Taxi_Analysis.ipynb      # Run All
```

## Headline findings
- 82% of pickups are in Manhattan; demand peaks at 18:00; median speed is about 9 mph from 08:00 to 18:59.
- Fare is about $2.54 + $2.09/mile + $0.28/minute (held-out R-squared 0.94); 126 trips at exactly $52 are flat-rate JFK trips.
- Cash tips are never recorded, so tip analysis uses card trips only (median tip 25.6% of fare).
- The yellow vs green tip gap (26.3% vs 11.8%) is largely a location and zero-tip effect: within Manhattan it narrows to 26.7% vs 22.3%.

## Cleaning summary
63 of 6,433 rows removed (1.0%): 51 zero-distance or non-positive-duration trips, 1 pickup outside March, 11 impossible speeds.
No duplicates were present. Genuine outliers were kept and handled with robust statistics.

## Limitations
One month, about 6,400-trip sample; each weekday occurs only 4-5 times; cash tips unrecorded; association, not causation.
