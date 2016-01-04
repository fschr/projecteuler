"""
The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

# First, load the words
with open("words.txt", "r") as words_file:
    words = words_file.read()[1:-1].split("\",\"")
    maximum_score = max([len(word) for word in words]) * 26

# We'll use a cache to generate the triangular numbers
triangular = [False] * (maximum_score + 1)
step, val = 2, 1
while val <= maximum_score:
    triangular[val] = True
    val += step
    step += 1

# define a function to score words
def score(word):
    return sum([ord(c) - 64 for c in word])

print(len([word for word in words if triangular[score(word)]]))
