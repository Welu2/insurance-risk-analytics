import pandas as pd

df = pd.read_csv("data/insurance_data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv(
    "data/insurance_data_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully.")