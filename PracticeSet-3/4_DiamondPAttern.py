'''Print a Diamond Pattern
Difficulty: Easy
Topics: Pattern Printing
Hint: Print a diamond pattern with stars (*). The pattern should include a single peak in the middle with symmetric rows above and below it.

Example 1: Input: n = 3
Output:

  *
 ***
*****
 ***
  *'''

def diamondPattern(n):
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)

    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)


diamondPattern(5)
