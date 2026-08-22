import numpy as np

# Problem 2: Search for a specific value in a NumPy array using where() function
print("=== Problem 2: Searching with np.where() ===")

# Create a NumPy array
arr = np.array([10, 20, 30, 20, 50, 20, 40])
print("Original Array:")
print(arr)

# Specific value to search
target_value = 20
print(f"\nSearching for value: {target_value}")

# Search using where()
result = np.where(arr == target_value)
print("Indices where value is found:", result[0])
print("Result tuple from np.where():", result)
