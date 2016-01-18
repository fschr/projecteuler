"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

# We'll make a sieve for all the prime numbers

LIMIT = 1000000
prime = [0, 0] + [1] * (LIMIT - 1)
for i in range(len(prime)):
    if prime[i]:
        for j in range(2 * i, len(prime), i):
            prime[j] = 0

# Shove all the valid primes into a different array
cache = [indx for indx, val in enumerate(prime) if val]

for n in range(33, LIMIT, 2):
    if prime[n]:
        continue
    valid = False
    twosquare = 1
    while 2 * twosquare * twosquare < n:
        tsq = 2 * twosquare * twosquare
        for p in cache:
            if tsq + p < n:
                continue
            if tsq + p > n:
                break
            if tsq + p == n:
                valid = True
                break
        if valid:
            break
        twosquare += 1
    if not valid:
        print(n)
        break
