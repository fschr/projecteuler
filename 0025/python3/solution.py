"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

# I'll use dynamic programming, even though it would be faster to approximate
# the number using the golden ratio and closed form

values = {1:1, 2:1}

def fib(n):
    if n in values:
        return values[n]
    number = fib(n - 1) + fib(n - 2)
    values[n] = number
    return number

i = 12
while True:
    i += 1
    if len(str(fib(i))) == 1000:
        print(i)
        break
