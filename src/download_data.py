"""Download the real-world dataset and record its provenance.

Dataset : NYC taxi trips, March 2019 (6,433 yellow and green cab trips)
Origin  : NYC Taxi & Limousine Commission (TLC) Trip Record Data,
          https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
Copy    : sample distributed in the seaborn-data repository
          https://github.com/mwaskom/seaborn-data  (file: taxis.csv)
Run     : python src/download_data.py
"""
from pathlib import Path
import hashlib
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
OUT = ROOT / "data" / "nyc_taxi_raw.csv"


def main() -> None:
    OUT.parent.mkdir(exist_ok=True)
    urllib.request.urlretrieve(URL, OUT)
    digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
    rows = sum(1 for _ in OUT.open()) - 1
    print(f"Saved {OUT.name}: {rows} rows | sha256 {digest[:16]}...")
    (ROOT / "data" / "SOURCE.md").write_text(
        "# Data source\n\n"
        "NYC Taxi & Limousine Commission trip records, March 2019 (yellow and green taxis).\n\n"
        f"- Downloaded from: {URL}\n"
        "- Original publisher: NYC TLC, https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page\n"
        f"- Rows: {rows}\n- SHA-256: {digest}\n\n"
        "The raw file is kept unmodified; all cleaning happens in the notebook.\n")


if __name__ == "__main__":
    main()
