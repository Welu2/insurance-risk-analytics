# Insurance Risk Analytics

## Project Overview

This project analyzes insurance risk, claim behavior, and profitability patterns using exploratory data analysis (EDA), data version control (DVC), statistical hypothesis testing, and machine learning techniques.

The analysis focuses on understanding:

- claim frequency
- claim severity
- loss ratios
- customer profitability
- regional risk trends
- demographic risk patterns
- predictive pricing and risk modeling

The project is designed to support data-driven insurance pricing and segmentation strategies.

---

## Project Objectives

The main objectives of this project are to:

- Understand insurance claim patterns
- Analyze portfolio profitability and loss ratios
- Identify geographic and demographic risk factors
- Explore temporal claim trends
- Perform statistical hypothesis testing on key business assumptions
- Build predictive models for claim severity and claim probability
- Develop a risk-based pricing framework
- Build reproducible data pipelines using DVC
- Prepare datasets for machine learning modeling

---

# Project Structure

```text
insurance-risk-analytics/
│
├── .dvc/
├── .github/workflows/
├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
│
├── reports/
├── scripts/
|   ├── clean_data.py
├── src/
│   ├── hypothesis_tests.py
│   └── modeling.py
│
├── tests/
├── dvc.yaml
├── requirements.txt
└── README.md