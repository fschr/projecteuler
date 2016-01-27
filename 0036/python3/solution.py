"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

# I suppose there are less palindromes less than 1,000,000 in base 10 than
# in base 2. So, we'll only iterate on the palindromes in base 10, and then
# check to see if they're also a palindrome in base 2.

palindromes10 = []

# We can form palindromes out of the string of digits ABC because
# ABCCBA, ABCBA, ABBA, ABA, and AA will always be
# palindromes.

for A in range(ord('1'), ord('9') + 1):
    for B in range(ord('0'), ord('9') + 1):
        for C in range(ord('0'), ord('9') + 1):        
            palindromes10.append(int(
                chr(A) + chr(B) + chr(C) + chr(C) + chr(B) + chr(A)
            ))
            palindromes10.append(int(
                chr(A) + chr(B) + chr(C) + chr(B) + chr(A)
            ))
        palindromes10.append(int(
            chr(A) + chr(B) + chr(B) + chr(A)
        ))
        palindromes10.append(int(
            chr(A) + chr(B) + chr(A)
        ))
    palindromes10.append(int(
        chr(A) + chr(A)
    ))
    palindromes10.append(int(chr(A)))

def binary_palindrome(n):
    reg = bin(n)[2:]
    flipped = "".join(list(reversed(bin(n)[2:])))
    if not reg.startswith("0") and not flipped.startswith("0"):
        return reg == flipped
    return False

print(sum([int(p) for p in palindromes10 if binary_palindrome(p)]))
