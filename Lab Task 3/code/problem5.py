n = int(input("Enter a number N: "))

a = 0
b = 1

print("Fibonacci numbers below", n, "are:")

while a < n:
    print(a)
    next_num = a + b
    a = b
    b = next_num