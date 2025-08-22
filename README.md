# NBA Player Stats Visualizer — exploring efficiency, usage, and scoring leaders with Python + Matplotlib

This repo is a lightweight, portfolio-ready project that pulls a small NBA player stats dataset and generates clean visualizations. It’s designed to show how simple code + data can turn into insights quickly — the same curiosity and problem‑solving mindset I bring to client conversations.

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

## Prospecting Angle (how I use this with technical buyers)
- *“I like to tinker — here’s a quick data viz I built. If we swapped the NBA data for your product metrics, what would you want to visualize first?”*
- *“I’m comfortable reading docs and wiring up basic scripts — that helps me ask sharper discovery questions when we talk integrations/APIs.”*
- *“I keep repos tidy with READMEs so anyone can run them — the same clarity I bring to customer communication and handoffs.”*

## Notes
- This is intentionally lightweight: clean code, clear README, sensible defaults.
- Want to swap the dataset? Replace `nba_stats_sample.csv` with your own data; columns are documented in the CSV header.