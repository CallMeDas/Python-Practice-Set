'''Print a Right-Angle Triangle of Stars
Difficulty: Easy
Topics: Pattern Printing
Hint: Print a right-angle triangle pattern of stars (*). Each row should contain an increasing number of stars, starting from 1 star in the first row.

Example 1: Input: n = 4
Output:

*
**
***
****'''

def starPattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print('*', end= '')
        print()


print(starPattern(4))