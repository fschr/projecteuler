"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindromify(x, y, z):
    return int(str(z) + str(y) + \
               str(x) + str(x) + \
               str(y) + str(z))

# Brute force :(
for one in range(9, 0, -1):
    for two in range(9, -1, -1):
        for three in range(9, -1, -1):
            num = palindromify(three, two, one)
            for a in range(100, 1000):
                for b in range(100, 1000):
                    if a * b == num:
                        print("{} * {} = {}".format(str(a), str(b), str(a * b)))
                        exit(0)
