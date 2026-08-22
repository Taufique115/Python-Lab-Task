import numpy as np

# Problem 5: Replace all negative values in a NumPy array with Zero
print("=== Problem 5: Replacing Negative Values with Zero ===")

# Create a NumPy array with positive and negative numbers
arr = np.array([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10])
print("Original Array:")
print(arr)

# Replace negative values with zero using boolean indexing
arr[arr < 0] = 0

print("\nArray after replacing negative values with Zero:")
print(arr)
