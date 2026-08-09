import os
import pandas as pd

# Locate data.csv relative to script directory
csv_path = os.path.join(os.path.dirname(__file__), "..", "data.csv")
if not os.path.exists(csv_path):
    csv_path = "data.csv"

# Load CSV file
df = pd.read_csv(csv_path)

print("--- First 5 Rows (head()) ---")
print(df.head())

print("\n--- Last 5 Rows (tail()) ---")
print(df.tail())

print("\n--- DataFrame Summary Info (info()) ---")
df.info()

