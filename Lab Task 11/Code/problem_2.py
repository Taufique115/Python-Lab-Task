import numpy as np

# Problem 2: Find the index of n'th repetition of an item in an array
print("=== Problem 2: Index of n'th Repetition of an Item ===")

# Create a NumPy array with repeated elements
arr = np.array([1, 3, 5, 3, 7, 3, 9, 3, 2, 3, 10])
item = 3
n = 3

print("Array:", arr)
print(f"Target Item: {item}")
print(f"Repetition (n): {n}")

# Find indices where item occurs
indices = np.where(arr == item)[0]

if len(indices) >= n:
    nth_index = indices[n - 1]
    print(f"\nAll indices of item '{item}': {indices}")
    print(f"Index of {n}'th repetition of item '{item}' is: {nth_index}")
else:
    print(f"\nItem '{item}' appears only {len(indices)} times, less than n = {n}")
