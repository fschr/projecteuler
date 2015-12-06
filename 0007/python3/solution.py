"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# Brute force :(

def special_prime(n):
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

count = 1
i = 3
while count < 10001:
    if special_prime(i):
        count += 1
    i += 2

print(i - 2p)
