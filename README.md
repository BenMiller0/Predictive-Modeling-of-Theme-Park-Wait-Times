# Predictive Modeling of Theme Park Wait Times

## Project Highlights
** ML Pipeline | 30+ Roller Coasters | 80+ Theme Parks **

**Key Finding:** Ride characteristics (speed, height, inversions) cannot meaningfully predict wait times - IP and theming likely the real demand drivers.

## Overview
Data engineering project analyzing roller coasters across theme parks to determine relationships between ride characteristics and guest demand. Built complete pipeline from web scraping to predictive modeling, proving physical telemetry alone cannot predict wait times.

## Tech Stack
- **Languages/Libraries:** Python, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **Web Scraping:** Selenium, BeautifulSoup4 (RCDB & Thrill Data)
- **ML/AI:** Linear Regression, Random Forest, feature engineering
- **Tools:** Jupyter Notebooks, Git

## Key Achievements
- **Data Pipeline:** Automated web scraping collecting 730+ coaster records
- **Data Validation:** Handled mixed units, missing values, and inconsistencies
- **ML Models:** Built predictive models quantifying physical telemetry impact
- **Feature Engineering:** Created thrill scores and relative park rankings

## Project Structure
```
├── data/
│   ├── raw/                 # Original scraped datasets
│   └── processed/           # Cleaned, analysis-ready data
│       ├── full_data.csv
│       ├── stats_cleaned.csv
│       └── wait_times_clean.csv
├── modules/
│   ├── add_missing.py       # Data cleaning utilities for rcdb thrill stats
│   ├── load_wait_times.py   # Wait times data processing
│   └── rcdb_scraper.py      # RCDB web scraping
├── PredicitingCoasterWaitTimes.ipynb  # Main analysis notebook
├── requirements.txt
└── README.md
```

## Setup & Installation
```bash
git clone https://github.com/BenMiller0/Predictive-Modeling-of-Theme-Park-Wait-Times.git
cd Predictive-Modeling-of-Theme-Park-Wait-Times
pip install -r requirements.txt
jupyter notebook PredicitingCoasterWaitTimes.ipynb
```

## Team
**Benjamin Miller, Johnathan Duong, Khang Nguyen, Naomika Nadkarni, Varun Prajapati**
