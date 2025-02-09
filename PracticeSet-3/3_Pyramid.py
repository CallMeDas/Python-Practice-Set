'''Print a Pyramid Pattern
Difficulty: Easy
Topics: Pattern Printing
Hint: Print a pyramid pattern with stars (*). The pyramid should have a single peak and each row should have an increasing number of stars, centered horizontally.

Example 1: Input: n = 3
Output:

  *
 ***
*****'''

def pyramidPattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

print(pyramidPattern(3))