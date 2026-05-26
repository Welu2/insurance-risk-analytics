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

The project is designed to support data-driven insurance pricing and segmentation strategies.

---

## Project Objectives

The main objectives of this project are to:

- Understand insurance claim patterns
- Analyze portfolio profitability and loss ratios
- Identify geographic and demographic risk factors
- Explore temporal claim trends
- Perform statistical hypothesis testing on key business assumptions
- Build reproducible data pipelines using DVC
- Prepare datasets for predictive risk modeling

---

# Project Structure

```text
insurance-risk-analytics/
│
├── .dvc/                         # DVC configuration
├── .github/workflows/            # GitHub Actions CI/CD
├── data/                         # Datasets tracked with DVC
├── notebooks/                    # Jupyter notebooks
│   ├── task1_eda.ipynb
│   ├── task2_data_cleaning.ipynb
│   └── task3_hypothesis_testing.ipynb
│
├── reports/                      # Generated reports and visualizations
├── scripts/                      # Data processing scripts
├── src/                          # Reusable Python modules
│   └── hypothesis_tests.py
│
├── tests/                        # Unit tests
│
├── dvc.yaml                      # DVC pipeline configuration
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd insurance-risk-analytics
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Data Version Control (DVC)

This project uses DVC to manage dataset versioning and ensure reproducibility.

## Initialize DVC

```bash
dvc init
```

## Pull Dataset

```bash
dvc pull
```

## Dataset Versions

- `insurance_data.csv` → raw dataset
- `insurance_data_cleaned.csv` → cleaned dataset

## Push Data to Remote Storage

```bash
dvc push
```

---

# Data Cleaning

The project includes preprocessing steps such as:

- duplicate removal
- missing value handling
- type corrections
- feature engineering

## Run Cleaning Script

```bash
python scripts/clean_data.py
```

---

# Exploratory Data Analysis (EDA)

The EDA phase includes:

- data summarization
- missing value analysis
- univariate analysis
- multivariate analysis
- geographic trend analysis
- outlier detection
- loss ratio analysis
- temporal trend visualization

## Key Variables Analyzed

- `TotalPremium`
- `TotalClaims`
- `CustomValueEstimate`
- `Province`
- `ZipCode`
- `VehicleType`
- `Gender`
- `AutoMake`

---

# Statistical Hypothesis Testing

Task 3 introduces A/B hypothesis testing to statistically validate insurance risk drivers.

## Risk KPIs

The project defines risk using:

### Claim Frequency

Proportion of policies with at least one claim.

```python
HasClaim = (TotalClaims > 0)
```

### Claim Severity

Average claim amount given a claim occurred.

### Margin

```python
Margin = TotalPremium - TotalClaims
```

---

# Hypotheses Tested

The following null hypotheses were evaluated:

| Hypothesis | KPI | Statistical Test |
|---|---|---|
| No risk difference across provinces | Claim Frequency | Chi-Square |
| No risk difference between zip codes | Claim Severity | Welch T-Test |
| No margin difference between zip codes | Margin | Welch T-Test |
| No risk difference between men and women | Claim Frequency | Chi-Square |

---

# Statistical Testing Utilities

Reusable statistical test functions are implemented in:

```text
src/hypothesis_tests.py
```

Functions include:

- `chi_square_test()`
- `t_test()`

These utilities support reusable and modular experimentation workflows.

---

# Controlled A/B Testing Design

To reduce confounding bias, comparisons were performed on statistically similar groups by controlling for:

- vehicle type
- cover type

This helps isolate the effect of the feature being tested.

---

# Hypothesis Testing Workflow

The workflow includes:

1. Load cleaned dataset
2. Engineer KPIs
3. Create controlled comparison groups
4. Run statistical tests
5. Evaluate p-values
6. Reject or fail to reject hypotheses
7. Generate business recommendations

---

# Example Results

| Hypothesis | Test | P-Value | Decision |
|---|---|---|---|
| Province Risk Difference | Chi-Square | 1.0000 | Fail to Reject H₀ |
| Zip Code Risk Difference | Welch T-Test | 0.3055 | Fail to Reject H₀ |
| Zip Code Margin Difference | Welch T-Test | 0.7968 | Fail to Reject H₀ |
| Gender Risk Difference | Chi-Square | 0.9638 | Fail to Reject H₀ |

---

# Business Interpretation

The statistical tests found no significant evidence of:

- regional risk differences
- zip code profitability differences
- gender-based claim differences

under the controlled experimental setup.

This suggests that:

- current pricing segmentation may already be reasonably calibrated
- additional variables may be needed to improve risk differentiation
- more granular behavioral or policy-level features could improve predictive performance

---

# Running Hypothesis Testing

```bash
jupyter notebook notebooks/task3_hypothesis_testing.ipynb
```

---

# Running Tests

```bash
python -m pytest
```

---

# Continuous Integration

GitHub Actions automatically:

- installs dependencies
- runs tests
- validates repository integrity
- checks project reproducibility

on every push and pull request.

---

# Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- DVC
- GitHub Actions
- Pytest
- Jupyter Notebook

---

# Future Improvements

Potential next steps include:

- predictive claim modeling
- loss ratio forecasting
- customer segmentation
- fraud detection
- generalized linear models (GLMs)
- gradient boosting models
- premium optimization

-