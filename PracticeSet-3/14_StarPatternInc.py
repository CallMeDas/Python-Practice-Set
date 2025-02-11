'''Print a Star Pattern with Increasing Width
Difficulty: Medium
Topics: Pattern Printing
Hint: Print a pattern where each row has an increasing width of stars.

Example 1: Input: n = 3
Output:

*
***
*****
'''

def starPattern(n):
    for i in range (n):
        print("*" * (2 * i + 1))


starPattern(3)