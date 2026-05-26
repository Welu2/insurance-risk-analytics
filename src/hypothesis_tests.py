import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind


def chi_square_test(df, group_col, target_col, group_a, group_b):
    """
    Chi-square test for categorical/binary outcomes.
    """

    subset = df[df[group_col].isin([group_a, group_b])]

    contingency = pd.crosstab(
        subset[group_col],
        subset[target_col]
    )

    chi2, p, dof, expected = chi2_contingency(contingency)

    return {
        "test": "Chi-Square",
        "p_value": p,
        "chi2": chi2,
        "dof": dof,
        "reject_null": p < 0.05
    }


def t_test(df, group_col, metric_col, group_a, group_b):
    """
    Welch t-test for numerical variables.
    """

    a = df[df[group_col] == group_a][metric_col].dropna()
    b = df[df[group_col] == group_b][metric_col].dropna()

    stat, p = ttest_ind(a, b, equal_var=False)

    return {
        "test": "Welch T-Test",
        "p_value": p,
        "t_statistic": stat,
        "reject_null": p < 0.05,
        "mean_a": a.mean(),
        "mean_b": b.mean()
    }
