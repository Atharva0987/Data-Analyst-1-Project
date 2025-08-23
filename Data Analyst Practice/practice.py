import pandas as pd
import numpy as np

df = pd.read_csv("sample_employee_data.csv")

# Convert Salary to numeric (force errors to NaN)
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Now you can safely fill NaN with mean
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# Handle Age too
df["Age"].fillna(df["Age"].median(), inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Remove negative or infinite values
df = df.replace([np.inf, -np.inf], np.nan)
df.dropna(subset=["Salary"], inplace=True)

# Outlier handling
salary_mean = df["Salary"].mean()
salary_std = df["Salary"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
df = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]

# Save cleaned file
df.to_csv("cleaned_sample_employee_data.csv", index=False)
print("Data cleaning completed! Saved as cleaned_sample_employee_data.csv")

