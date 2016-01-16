"""
An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910[1]112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

# Quick old brute force solution

MAX = 1000000 # There's no way that
              # d_1000000 will require a string 123...n, n > 1000000

s = "".join([str(n) for n in range(MAX)])

print(
    int(s[10]) * \
    int(s[100]) * \
    int(s[1000]) * \
    int(s[10000]) * \
    int(s[100000]) * \
    int(s[1000000])
)
