import numpy as np

# Problem 4: Get positions where elements of two arrays match
print("=== Problem 4: Finding Matching Positions in Two Arrays ===")

# Create two 1D NumPy arrays
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print("Array A:", a)
print("Array B:", b)

# Get matching positions using np.where()
matching_positions = np.where(a == b)[0]

print("\nMatching Positions (Indices):", matching_positions)
print("Matching Elements:", a[matching_positions])
