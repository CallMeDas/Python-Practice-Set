'''Print a Pattern of Consecutive Numbers
Difficulty: Medium
Topics: Matrix Pattern
Hint: Print a matrix of consecutive numbers starting from 1, filling rows sequentially.

Example 1: Input: n = 3
Output:

1 2 3
4 5 6
7 8 9
'''

def consecutiveNo(n):
    num = 1
    for i in range(n):
        for j in range (n):
            print(num, end= ' ')
            num += 1
        print()


consecutiveNo(3)