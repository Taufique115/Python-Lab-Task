import pandas as pd

# Load data into a Pandas DataFrame
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)

print("--- Full DataFrame ---")
print(df)

# Select rows 0 and 2 using "loc" attribute
selected_rows = df.loc[[0, 2]]
print("\n--- Selected Rows 0 and 2 using loc ---")
print(selected_rows)
