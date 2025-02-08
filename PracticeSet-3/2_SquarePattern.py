'''Print a Square of Stars
Difficulty: Easy
Topics: Pattern Printing
Hint: Print a square pattern of stars (*). Each row and column should have the same number of stars.

Example 1: Input: n = 5
Output:

*****
*****
*****
*****
*****'''

def squarePattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print('*', end= '')
        print()


print(squarePattern(5))