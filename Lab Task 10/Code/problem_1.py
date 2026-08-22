import numpy as np

# Problem 1: Create another shape from a NumPy array without changing its data
print("=== Problem 1: Reshaping a NumPy Array ===")

# Create a 1D NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(arr)
print("Original Shape:", arr.shape)

# Reshape array to a 2D array of shape (2, 3) without changing data
reshaped_2x3 = arr.reshape(2, 3)
print("\nReshaped Array (2x3):")
print(reshaped_2x3)
print("New Shape:", reshaped_2x3.shape)

# Reshape array to a 2D array of shape (3, 2)
reshaped_3x2 = arr.reshape(3, 2)
print("\nReshaped Array (3x2):")
print(reshaped_3x2)
print("New Shape:", reshaped_3x2.shape)
