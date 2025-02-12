'''Print an Inverted Pyramid Pattern with Characters
Difficulty: Medium
Topics: Pattern Printing
Hint: Print an inverted pyramid pattern using characters. Each row should have decreasing characters from the top row.

Example 1: Input: n = 3
Output:

CCCCC
 BBB
  A
'''

def pyramidChars(n):
    for i in range(n):
        print(" " * i + chr(65 + n - 1 - i) * (2 * (n - i) - 1))

pyramidChars(3)
