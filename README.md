# Insurance Risk Analytics

## Project Overview

This project analyzes insurance risk, claim behavior, and profitability patterns using exploratory data analysis (EDA), data version control (DVC), hypothesis testing, and machine learning techniques.

The analysis focuses on understanding claim severity, claim frequency, loss ratios, and regional risk trends across insurance customers and vehicle categories.

---

## Objectives

* Understand insurance claim patterns
* Analyze portfolio loss ratios
* Identify geographic and demographic risk factors
* Explore temporal claim trends
* Build reproducible data pipelines using DVC
* Prepare data for predictive risk modeling

---

## Project Structure

```text id="zjlwmk"
insurance-risk-analytics/
│
├── .dvc/                     # DVC configuration
├── .github/workflows/        # GitHub Actions CI
├── data/                     # Dataset metadata tracked by DVC
├── notebooks/                # Jupyter notebooks
├── reports/                  # Generated reports and figures
├── scripts/                  # Data processing scripts
├── src/                      # Reusable Python modules
├── tests/                    # Unit tests
│
├── dvc.yaml                  # DVC pipeline configuration
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore
```

---

## Installation

Clone the repository:

```bash id="tjlwm0"
git clone <your-repository-url>
cd insurance-risk-analytics
```

Install dependencies:

```bash id="8jlwm3"
pip install -r requirements.txt
```

---

## Exploratory Data Analysis (EDA)

The project includes:

* Data summarization
* Missing value analysis
* Univariate and multivariate analysis
* Geographic trend analysis
* Outlier detection
* Loss ratio analysis
* Temporal trend visualization

Key variables analyzed include:

* TotalPremium
* TotalClaims
* CustomValueEstimate
* Province
* VehicleType
* Gender
* AutoMake

---

## Data Version Control (DVC)

This project uses DVC for dataset versioning and reproducibility.

### Initialize DVC

```bash id="jlwm3p"
dvc init
```

### Pull Dataset

```bash id="jlwm6a"
dvc pull
```

### Dataset Versions

* `insurance_data.csv` → raw dataset
* `insurance_data_cleaned.csv` → cleaned dataset

### Push Data to Remote Storage

```bash id="4jlwmn"
dvc push
```

---

## Running the Data Cleaning Script

```bash id="jlwm4s"
python scripts/clean_data.py
```

---

## Running Tests

```bash id="jlwm2x"
python -m pytest
```

---

## Continuous Integration

GitHub Actions is configured to automatically:

* install dependencies
* run tests
* validate project integrity on every push

---

## Key Insights from EDA

* Certain provinces exhibit significantly higher loss ratios
* High-value vehicles tend to show larger claim severity
* Outliers exist in TotalClaims and CustomValueEstimate
* Claim frequency and severity vary over time
* Vehicle make influences average claim amount

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* DVC
* GitHub Actions
* Pytest

---
