# Nigeria Literacy Rate Analysis (1991–2024)

An interactive data analysis dashboard exploring literacy trends in Nigeria, with a focus on gender and wealth-based disparities. Built as an exploratory tool to surface where literacy gaps are widest — and where interventions might matter most.

**Live app:** [streamlit link]

---

## Overview

Nigeria's literacy rate is often reported as a single national figure, which hides where the real gaps are. This project breaks the number down by **gender** and **household wealth** to ask a more useful question: *is the literacy gap in Nigeria really about gender — or is it about economic access?*

Key finding: the gender literacy gap (16 points) is significantly narrower than the wealth-based gap (72 points between the poorest and richest quintiles) — suggesting economic inclusion may be a stronger lever for improving literacy outcomes than gender-focused interventions alone.

## Features

- **Adult vs Youth toggle** — compare literacy trends across age groups (1991–2024)
- **Gender breakdown** — male vs female literacy rates over time, with headline gap metrics
- **Wealth quintile breakdown** — literacy among young women by household wealth (poorest to richest)
- **Interactive charts** — hover for exact values, zoom/pan (built with Plotly)

## Data Sources

| Source | Coverage | Notes |
|---|---|---|
| [World Bank Open Data](https://data.worldbank.org) — Nigeria education indicators | 1991–2024, national level | Primary time-series; sparse years reflect actual survey/estimate availability, not missing data |
| [UNICEF/NBS Nigeria MICS4 (2011)](https://mics.unicef.org/country-profiles/nigeria/4131) | Young women 15–24, by wealth quintile | Used for the wealth-quintile comparison; figures manually extracted from the published factsheet |

**A note on data quality:** literacy estimates for Nigeria vary noticeably across sources (World Bank, MICS, DHS) due to differing survey methodologies and years. This project uses World Bank data as its primary series for consistency over time, with MICS4 used specifically for the wealth-quintile angle, which World Bank data doesn't break out. Where sources disagree, that's flagged rather than smoothed over.

## Tech Stack

- Python
- Streamlit — app framework
- Pandas — data cleaning and reshaping
- Plotly — interactive visualization

## Methodology

1. Sourced raw indicator data from the World Bank's education dataset for Nigeria
2. Filtered to literacy-specific indicators (adult/youth, male/female)
3. Reshaped from long to wide format for time-series analysis
4. Dropped years with incomplete gender-pair data to ensure clean comparisons
5. Cross-referenced with MICS4 (2011) wealth-quintile data to add a second analytical lens
6. Built an interactive Streamlit dashboard for exploration

## Running Locally

```bash
git clone https://github.com/bibexaliyy/nigeria-literacy-analysis.git
cd nigeria-literacy-analysis
pip install -r requirements.txt
streamlit run app.py
```

## Limitations & Future Work

- Literacy survey years are sparse (not annual), consistent with how these surveys are actually conducted — trends should be read as directional, not precisely continuous
- Wealth-quintile data is from a single survey year (2011) rather than a time series
- State/LGA-level breakdown not yet included — planned as a future addition
- No confidence intervals currently shown on survey-based estimates

## Author

Habiba — [LinkedIn](#) · [GitHub](#)

Built as part of an ongoing effort to combine data analysis skills with civic/education advocacy work in Nigeria.
