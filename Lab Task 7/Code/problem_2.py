try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        raise TypeError("Inputs must be numerical")

    result = float(num1) + float(num2)
    print("Sum:", result)

except TypeError as e:
    print("TypeError:", e)