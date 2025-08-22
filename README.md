# NBA Player Stats Visualizer — exploring efficiency, usage, and scoring leaders with Python + Matplotlib

This repo is a lightweight, portfolio-ready project that pulls a small NBA player stats dataset and generates clean visualizations. 

## What this does
- Loads a small (synthetic) NBA player stats dataset
- Creates two charts:
  1. **Top Scorers** (bar chart — points per game)
  2. **Usage vs. True Shooting** (scatter — efficiency vs. volume)

## Quickstart
```bash
# 1) (optional) Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the script to generate charts in /charts
python app.py
```

## Files
- `app.py` — main script that loads data and generates charts
- `nba_stats_sample.csv` — sample dataset used by the script
- `requirements.txt` — Python dependencies
- `charts/` — output folder with PNGs after you run the script

## Notes
- This is intentionally lightweight: clean code, clear README, sensible defaults.
- Want to swap the dataset? Replace `nba_stats_sample.csv` with your own data; columns are documented in the CSV header.
