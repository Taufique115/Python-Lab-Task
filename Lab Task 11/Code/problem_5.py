import numpy as np

# Problem 5: Summation, product, and difference using sum(), prod(), and diff()
print("=== Problem 5: Summation, Product, and Difference Operations ===")

# Create two NumPy arrays
x = np.array([10, 20, 30, 40])
y = np.array([2, 4, 6, 8])

print("Array X:", x)
print("Array Y:", y)

# Summation using np.sum()
total_sum = np.sum([x, y])
elementwise_sum = np.sum([x, y], axis=0)
print("\nTotal Summation of all elements (np.sum([x, y])):", total_sum)
print("Element-wise Summation (np.sum([x, y], axis=0)):", elementwise_sum)

# Product using np.prod()
total_prod = np.prod([x, y])
elementwise_prod = np.prod([x, y], axis=0)
print("\nTotal Product of all elements (np.prod([x, y])):", total_prod)
print("Element-wise Product (np.prod([x, y], axis=0)):", elementwise_prod)

# Difference using np.diff()
diff_between_arrays = np.diff([x, y], axis=0)[0]
diff_consecutive_x = np.diff(x)
print("\nDifference between Array Y and Array X (np.diff([x, y], axis=0)):", diff_between_arrays)
print("Difference between consecutive elements of X (np.diff(x)):", diff_consecutive_x)
