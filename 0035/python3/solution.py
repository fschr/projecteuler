"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

N = 1000000

# First, make a sieve
sieve = [1] * (N + 1)
sieve[0] = 0
sieve[1] = 0
for i in range(2, len(sieve)):
    if sieve[i]:
        for j in range(2 * i, len(sieve), i):
            sieve[j] = 0

# make a function to rotato a brotato
def rotato(n):
    for i in range(len(str(n))):
        if not sieve[int(str(n)[i:] + str(n)[:i])]:
            return False
    return True

# Now find the circular primes
circs = set()
for number, prime in enumerate(sieve):
    if rotato(number):
        circs.add(number)

print(len(circs))
