'''Print a Hollow Square of Stars
Difficulty: Easy
Topics: Pattern Printing
Hint: Print a hollow square pattern with stars (*). The border of the square should be filled with stars while the inner part should be empty.

Example 1: Input: n = 5
Output:

*****
*   *
*   *
*   *
*****
'''

def hallowSquare(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")

hallowSquare(5)
