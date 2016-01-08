"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

# We'll use a sieve for this
# I'll try SIEVE_MAX = 100000 because it seems reasonable
# It seems reasonable because as N grows, it's "harder" for a number to be a
# truncatable prime

SIEVE_MAX = 1000000
prime = [1] * (SIEVE_MAX + 1)
prime[0] = 0
prime[1] = 0
for number in range(2, len(prime)):
    if number:
        for multiple in range(2 * number, len(prime), number):
            prime[multiple] = 0

# Let's define the truncatable function
def truncatable(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return False
    for i in range(len(str(n))):
        if not prime[int(str(n)[i:])]:
            return False
    for i in range(len(str(n)) - 1):
        if not prime[int(str(n)[0:-i - 1])]:
            return False
    return True

# We either find all 11 truncatable primes, or we hit the sieve limit
print(sum(
    [number for number, is_prime in enumerate(prime) if truncatable(number)]
))
