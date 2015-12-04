# No dynamic programming, no fun :(
a, b = 1, 2
_sum = 0
while b < 4000000:
    _sum += b
    a, b = b, a + b
    a, b = b, a + b
    a, b = b, a + b
    # only every third element is even
print(_sum)

