'''Print a Pattern with Concentric Squares
Difficulty: Medium
Topics: Pattern Printing
Hint: Print a pattern with concentric squares using stars. The outer square should be larger and each subsequent square should be centered inside.

Example 1: Input: n = 5
Output:

*****
*   *
*   *
*   *
*****
'''

def concentricSquares(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

concentricSquares(5)
