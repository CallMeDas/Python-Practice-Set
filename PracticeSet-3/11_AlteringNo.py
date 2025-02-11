'''Print a Pattern of Alternating 0s and 1s
Difficulty: Medium
Topics: Matrix Pattern
Hint: Print a matrix where elements alternate between 0 and 1. The pattern should alternate both row-wise and column-wise.

Example 1: Input: n = 4
Output:

0101
1010
0101
1010
'''

def alteringPattern(n):
    for i in range(n):
        for j in range(n):
            print((i + j) %2 , end= '')
        print()



alteringPattern(4)