"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
n = 600851475143
while n % 2 == 0:
    n //= 2
i = 3
gpf = None
while i <= n:
    while n % i == 0:
        n //= i
        gpf = i
    i += 2
print(gpf)
