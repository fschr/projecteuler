import sys

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

dictionary = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}

def english(n):
    if n == 1000:
        return "one " + dictionary[1000]
    elif n >= 100 and n < 1000:
        if n % 100 == 0:
            return "{} {}".format(dictionary[n // 100], dictionary[100])
        else:
            return "{} {} and ".format(
                dictionary[n // 100], dictionary[100]
            ) + english( int(str(n)[1:]) )
    elif n >= 20 and n < 100:
        if n % 10 == 0:
            return dictionary[n]
        else:
            return "{}-{}".format(
                dictionary[10 * (n // 10)],
                dictionary[int(str(n)[1:])],
            )
    elif n < 20:
        return dictionary[n]

def number_of_letters_within_string_s(s):
    return len(s.strip().replace(" ", "-").replace("-", ""))

print(sum([number_of_letters_within_string_s(english(_____)) for _____ in range(1, 1001)]))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            print(english(int(sys.argv[1])))
        except:
            print("You're a bastard with no manners,\nand not a dook of an idea how to comport\nyourself public-wise, O my brother.")
