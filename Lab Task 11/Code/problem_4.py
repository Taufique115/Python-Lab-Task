import numpy as np

# Problem 4: Summation, subtraction, multiplication, and division using add(), subtract(), multiply(), and divide()
print("=== Problem 4: Basic Arithmetic Operations on NumPy Arrays ===")

# Create two NumPy arrays
x = np.array([10, 20, 30, 40])
y = np.array([2, 4, 5, 8])

print("Array X:", x)
print("Array Y:", y)

# Summation using np.add()
summation = np.add(x, y)
print("\nSummation (np.add):", summation)

# Subtraction using np.subtract()
subtraction = np.subtract(x, y)
print("Subtraction (np.subtract):", subtraction)

# Multiplication using np.multiply()
multiplication = np.multiply(x, y)
print("Multiplication (np.multiply):", multiplication)

# Division using np.divide()
division = np.divide(x, y)
print("Division (np.divide):", division)
