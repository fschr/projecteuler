"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

# If a number is hexagonal, then it must be triangle
# So we don't need to define a hexagonal function, because we'll only check
# hexagonal numbers

# So, let's define a pentagonal function
# It's slow to iterate through a bunch of numbers
# We can do this in one step, if we find the inverse function

# Let N = n(3n - 1)/2
#    2N = n(3n - 1)
#    2N = 3n^2 - n
#    3n^2 - n - 2N = 0
#
# A = 3, B = -1, C = -2N
#
# (-b +- sqrt(b^2 - 4ac)) / (2a)
#
# (1 +- sqrt(1 + 24N)) / 6 = some real number
#
# If that real number is an integer, then the number is pentagonal
def pentagonal(n):
    return (1 + (1 + 24*n)**0.5) / 6 == int((1 + (1 + 24*n)**0.5) / 6)

# We need to start on H_144
n = 144

while True:
    hexagonal_number = n*(2*n - 1)
    if pentagonal(hexagonal_number):
        print(hexagonal_number)
        break
    n += 1
