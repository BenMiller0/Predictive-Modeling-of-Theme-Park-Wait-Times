# Predictive Modeling of Theme Park Wait Times

## Project Highlights
** Data Science Project | 730+ Roller Coasters | 80+ Theme Parks | ML Pipeline**

**Key Finding:** Ride characteristics (speed, height, inversions) cannot predict wait times - IP and theming are the real demand drivers.

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
- **Key Insight:** Disproved hypothesis - physical characteristics explain minimal variance in wait times

## Results
- **Finding:** Other factors such as IP and theming are liekly primary demand drivers, not ride intensity
- **Data:** 730+ records across major theme park chains
- **Completeness:** 95% data quality through automated cleaning

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
├── results/                 # Analysis outputs and visualizations
├── PredicitingCoasterWaitTimes.ipynb  # Main analysis notebook
├── requirements.txt
└── README.md
```

## Technical Implementation
- **Data Collection:** Automated extraction from RCDB.com and Thrill-Data.com
- **Feature Engineering:** Thrill score formula and within-park rankings
- **ML Approach:** Linear regression and Random Forest with cross-validation
- **Thrill Score:** `(#inversions × 15) + (Height/5) + (Speed/5) + (Length/150)`

## Setup & Installation
```bash
git clone https://github.com/BenMiller0/Predictive-Modeling-of-Theme-Park-Wait-Times.git
cd Predictive-Modeling-of-Theme-Park-Wait-Times
pip install -r requirements.txt
jupyter notebook PredicitingCoasterWaitTimes.ipynb
```

## 👥 Team
**Benjamin Miller** - Lead Developer, Data Architecture, ML Engineering  
**Johnathan Duong** - Web Scraping, Data Processing, Analysis  
**Khang Nguyen** - Feature Engineering, Statistical Modeling  
**Naomika Nadkarni** - Data Validation, Quality Assurance  
**Varun Prajapati** - Research, Methodology, Analysis
