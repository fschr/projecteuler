"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

# Brute force :(
# Some optimizations

best_count = 0
best_p = 0

for p in range(10, 1001, 2):
    # a^2 + b^2 = c^2
    # and
    # a + b + c = p
    count = 0
    for a in range(1, p - 1):
        for b in range(a, p - 1 - a):
            c = p - a - b
            if a*a + b*b == c*c:
                count += 1
    if count > best_count:
        best_count = count
        best_p = p
            
print(best_p)
