import numpy as np

# Problem 1: Find the K-smallest values of a NumPy array
print("=== Problem 1: Finding K-Smallest Values in Array ===")

# Create an unsorted NumPy array
arr = np.array([12, 5, 8, 1, 19, 3, 27, 2, 14])
print("Original Array:")
print(arr)

k = 3
print(f"\nFinding {k}-smallest values:")

# Method 1: Using np.partition()
k_smallest_partition = np.partition(arr, k)[:k]
print(f"K-smallest values (using np.partition): {k_smallest_partition}")

# Method 2: Sorted K-smallest values
k_smallest_sorted = np.sort(arr)[:k]
print(f"K-smallest values (sorted): {k_smallest_sorted}")
