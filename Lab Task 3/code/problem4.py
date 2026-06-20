def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

total = 0
for number in range(2, 1000):
    if is_prime(number):
        total = total + number

print("Sum of all primes below 1000 is:", total)