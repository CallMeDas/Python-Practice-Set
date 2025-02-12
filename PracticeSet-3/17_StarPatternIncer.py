''' Print a Pyramid Pattern of Increasing Stars
Difficulty: Medium
Topics: Pattern Printing
Hint: Print a pyramid pattern where each row increases in the number of stars.

Example 1: Input: n = 3
Output:

  *
 ***
*****
'''

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


pyramid(3)
