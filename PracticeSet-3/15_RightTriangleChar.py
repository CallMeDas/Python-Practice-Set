''' Print a Right-Angle Triangle Pattern with Characters
Difficulty: Medium
Topics: Pattern Printing
Hint: Print a right-angle triangle pattern using characters. Each row should contain the same character repeated according to the row number.

Example 1: Input: n = 3
Output:

A
BB
CCC
'''

def characterTriangle(n):
    for i in range(n):
        print(chr(65 + i) * (i + 1))

characterTriangle(3)
