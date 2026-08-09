import os
import pandas as pd

# Locate titanic.csv relative to script directory
csv_path = os.path.join(os.path.dirname(__file__), "..", "titanic.csv")
if not os.path.exists(csv_path):
    csv_path = "titanic.csv"

# Problem 4: Load Titanic dataset and apply data cleaning techniques
print("=== Loading Titanic Dataset ===")
titanic = pd.read_csv(csv_path)

print("\n--- Initial Dataset Info ---")
print("Shape:", titanic.shape)
print("Missing values per column:\n", titanic.isnull().sum())

# 1. Handling Duplicates
initial_len = len(titanic)
titanic = titanic.drop_duplicates()
print(f"\n--- 1. Removed Duplicates: {initial_len - len(titanic)} duplicates dropped ---")

# 2. Handling Empty Cells (Missing Values)
if "Age" in titanic.columns:
    age_mean = titanic["Age"].mean()
    titanic["Age"] = titanic["Age"].fillna(age_mean)

if "Embarked" in titanic.columns:
    embarked_mode = titanic["Embarked"].mode()[0] if not titanic["Embarked"].mode().empty else "S"
    titanic["Embarked"] = titanic["Embarked"].fillna(embarked_mode)

if "Cabin" in titanic.columns:
    titanic["Cabin"] = titanic["Cabin"].fillna("Unknown")

print("\n--- 2. Handled Empty Cells ---")
print("Remaining missing values:\n", titanic.isnull().sum())

# 3. Handling Wrong Format
if "Age" in titanic.columns:
    titanic["Age"] = titanic["Age"].astype(float).round(1)

if "Fare" in titanic.columns:
    titanic["Fare"] = titanic["Fare"].astype(float).round(2)

print("\n--- 3. Corrected Data Formats ---")
print(titanic.dtypes)

# 4. Handling Wrong Data / Outliers
if "Age" in titanic.columns:
    titanic.loc[titanic["Age"] > 100, "Age"] = titanic["Age"].median()
    titanic.loc[titanic["Age"] < 0, "Age"] = titanic["Age"].median()

if "Fare" in titanic.columns:
    titanic.loc[titanic["Fare"] < 0, "Fare"] = titanic["Fare"].median()

print("\n--- 4. Corrected Wrong Data / Outliers ---")
print("Cleaned Dataset Head:")
print(titanic.head())

# Save cleaned dataset
save_path = os.path.join(os.path.dirname(__file__), "..", "cleaned_titanic.csv")
titanic.to_csv(save_path, index=False)
print("\nCleaned dataset saved successfully as 'cleaned_titanic.csv'")
