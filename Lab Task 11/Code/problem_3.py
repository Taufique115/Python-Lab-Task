import numpy as np

# Problem 3: Compute sum of each column and sum of each row in a NumPy array
print("=== Problem 3: Row-wise and Column-wise Sums ===")

# Create a 2D NumPy array (matrix)
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("2D NumPy Array (Matrix):")
print(mat)

# Compute column-wise sum (axis=0)
col_sum = np.sum(mat, axis=0)
print("\nSum of each column (axis=0):", col_sum)

# Compute row-wise sum (axis=1)
row_sum = np.sum(mat, axis=1)
print("Sum of each row (axis=1):", row_sum)
