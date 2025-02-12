'''Print a Checkerboard Pattern
Difficulty: Medium
Topics: Matrix Pattern
Hint: Print a checkerboard pattern with two different characters alternating.

Example 1: Input: n = 4
Output:

XOXOXO
OXOXOX
XOXOXO
OXOXOX
'''


def checkerboard(n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("X", end="")
            else:
                print("O", end="")
        print()

checkerboard(4)
