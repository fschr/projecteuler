"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from math import factorial

# There are 9! permutations starting with each digit,
# so divide 1000000 by 9! to get the first digit

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number = 999999 # there is a zeroth entry

solution = ""

while len(digits) > 1:
    this_digit = digits[number // factorial(len(digits) - 1)]
    number %= factorial(len(digits) - 1)
    digits.remove(this_digit)
    solution += str(this_digit)

print(solution)
