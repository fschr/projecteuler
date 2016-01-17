"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = 	
n!
/
r!(n−r)!
	,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""

# This is a good math problem, but I'll solve it with dynamic programming instead

from math import factorial

cache = dict()

def choose(n, r):
    if n in cache:
        n_factorial = cache[n]
    else:
        n_factorial = factorial(n)
        cache[n] = n_factorial
    if r in cache:
        r_factorial = cache[r]
    else:
        r_factorial = factorial(r)
        cache[r] = r_factorial
    if n - r in cache:
        n_minus_r_factorial = cache[n-r]
    else:
        n_minus_r_factorial = factorial(n - r)
        cache[n - r] = n_minus_r_factorial
    return int(n_factorial / (r_factorial * (n_minus_r_factorial)))

count = 0
for n in range(1, 100 + 1):
    for r in range(2, n):
        if choose(n, r) > 1000000:
            count += 1

print(count)

# Runs in the blink of an eye :-)
