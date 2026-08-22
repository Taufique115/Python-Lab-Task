import numpy as np

# Problem 3: Print all even numbers in a NumPy array using the filtering feature
print("=== Problem 3: Boolean Filtering for Even Numbers ===")

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18])
print("Original Array:")
print(arr)

# Boolean filtering for even numbers
even_numbers = arr[arr % 2 == 0]

print("\nFiltered Even Numbers:")
print(even_numbers)
