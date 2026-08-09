import pandas as pd

# Load data into a Pandas Series
calories = {"day1": 420, "day2": 380, "day3": 390}
series = pd.Series(calories)

print("--- Pandas Series ---")
print(series)

# Find the summation of calories
total_calories = series.sum()
print("\nSummation of Calories:", total_calories)
