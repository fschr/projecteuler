"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

# We'll make a sieve for the primes
PRIME_LIMIT = 1000000
prime = [0, 0] + [1] * (PRIME_LIMIT - 1)
for i in range(len(prime)):
    if prime[i]:
        for j in range(2 * i, len(prime), i):        
            prime[j] = 0

# generate the b range
# b must be prime since for n = 0, n * n + a * n + b = b
b_range = [indx for indx, val in enumerate(prime) if indx < 1000 and val]

def func(a, b, n):
    return n * n + a * n + b

max_count = 0
product = 0
for a in range(-999, 1000):
    for b in b_range:
        n = 0
        count = 0
        while prime[func(a, b, n)]:
            count += 1
            n += 1
        if count > max_count:
            max_count = count
            product = a * b

print(product)
